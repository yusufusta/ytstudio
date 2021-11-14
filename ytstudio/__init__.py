from hashlib import sha1
import time
import aiohttp
import asyncio
import aiofiles
from pyquery import PyQuery as pq
import js2py
import js2py.pyjs
import random
import os
import json


class Studio:
    YT_STUDIO_URL = "https://studio.youtube.com"
    USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36"
    TRANSFERRED_BYTES = 0
    CHUNK_SIZE = 1024*2

    def __init__(self, cookies: dict = {'VISITOR_INFO1_LIVE': '', 'PREF': '', 'LOGIN_INFO': '', 'HSID': '', 'SAPISID': '', 'YSC': '', 'SIDCC': ''}, session_token: str = ""):
        self.SAPISIDHASH = self.generateSAPISIDHASH(cookies['SAPISID'])
        self.Cookie = " ".join([f"{c}={cookies[c]};" for c in cookies.keys()])
        self.HEADERS = {
            'Authorization': f'SAPISIDHASH {self.SAPISIDHASH}',
            'Content-Type': 'application/json',
            'Cookie': self.Cookie,
            'X-Origin': self.YT_STUDIO_URL,
            'User-Agent': self.USER_AGENT
        }
        self.session = aiohttp.ClientSession(headers=self.HEADERS)
        self.loop = asyncio.get_event_loop()
        self.config = {}
        self.js = js2py.EvalJs()
        self.js.execute("var window = {};")
        self.session_token = session_token

    def __del__(self):
        self.loop.create_task(self.session.close())

    def generateSAPISIDHASH(self, SAPISID) -> str:
        hash = f"{round(time.time())} {SAPISID} {self.YT_STUDIO_URL}"
        sifrelenmis = sha1(hash.encode('utf-8')).hexdigest()
        return f"{round(time.time())}_{sifrelenmis}"

    async def getMainPage(self) -> str:
        page = await self.session.get(self.YT_STUDIO_URL)
        return await page.text("utf-8")

    async def login(self) -> bool:
        page = await self.getMainPage()
        _ = pq(page)
        script = _("script")
        if len(script) < 1:
            raise Exception("Didn't find script. Can you check your cookies?")
        script = script[0].text
        self.js.execute(f"{script} window.ytcfg = ytcfg;")

        INNERTUBE_API_KEY = self.js.window.ytcfg.data_.INNERTUBE_API_KEY
        CHANNEL_ID = self.js.window.ytcfg.data_.CHANNEL_ID
        # DELEGATED_SESSION_ID = js.window.ytcfg.data_.DELEGATED_SESSION_ID Looking Google removed this key

        if INNERTUBE_API_KEY == None or CHANNEL_ID == None:
            raise Exception(
                "Didn't find INNERTUBE_API_KEY or CHANNEL_ID. Can you check your cookies?")
        self.config = {'INNERTUBE_API_KEY': INNERTUBE_API_KEY,
                       'CHANNEL_ID': CHANNEL_ID, 'data_': self.js.window.ytcfg.data_}
        return True

    def generateHash(self) -> str:
        harfler = list(
            '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
        keys = ['' for i in range(0, 36)]
        b = 0
        c = ""
        e = 0

        while e < 36:
            if 8 == e or 13 == e or 18 == e or 23 == e:
                keys[e] = "-"
            else:
                if 14 == e:
                    keys[e] = "4"
                elif 2 >= b:
                    b = round(33554432 + 16777216 * random.uniform(0, 0.9))
                c = b & 15
                b = b >> 4
                keys[e] = harfler[c & 3 | 8 if 19 == e else c]
            e += 1

        return "".join(keys)

    async def fileSender(self, file_name):
        async with aiofiles.open(file_name, 'rb') as f:
            while True:
                chunk = await f.read(self.CHUNK_SIZE)
                if not chunk:
                    break
                if self.progress != None:
                    self.TRANSFERRED_BYTES += len(chunk)
                    self.progress(self.TRANSFERRED_BYTES,
                                  os.path.getsize(file_name))
                yield chunk

    async def uploadFileToYoutube(self, upload_url, file_path):
        self.TRANSFERRED_BYTES = 0

        uploaded = await self.session.post(upload_url,  headers={
            "Content-Type": "application/x-www-form-urlencoded;charset=utf-8'",
            "x-goog-upload-command": "upload, finalize",
            "x-goog-upload-file-name": f"file-{round(time.time())}",
            "x-goog-upload-offset": "0",
            "Referer": self.YT_STUDIO_URL,
        }, data=self.fileSender(file_path), timeout=None)
        _ = await uploaded.text("utf-8")
        _ = json.loads(_)
        return _['scottyResourceId']

    async def uploadVideo(self, file_name, title=f"New Video {round(time.time())}", description='This video uploaded by github.com/yusufusta/ytstudio', privacy='PRIVATE', draft=False, progress=None):
        self.progress = progress
        frontEndUID = f"innertube_studio:{self.generateHash()}:0"

        uploadRequest = await self.session.post("https://upload.youtube.com/upload/studio",
                                                headers={
                                                    "Content-Type": "application/x-www-form-urlencoded;charset=utf-8'",
                                                    "x-goog-upload-command": "start",
                                                    "x-goog-upload-file-name": f"file-{round(time.time())}",
                                                    "x-goog-upload-protocol": "resumable",
                                                    "Referer": self.YT_STUDIO_URL,
                                                },
                                                json={'frontendUploadId': frontEndUID})

        uploadUrl = uploadRequest.headers.get("x-goog-upload-url")
        scottyResourceId = await self.uploadFileToYoutube(uploadUrl, file_name)

        upload = await self.session.post(
            f"https://studio.youtube.com/youtubei/v1/upload/createvideo?alt=json&key={self.config['INNERTUBE_API_KEY']}",
            json={
                "channelId": self.config['CHANNEL_ID'],
                "resourceId": {
                    "scottyResourceId": {
                        "id": scottyResourceId
                    }
                },
                "frontendUploadId": frontEndUID,
                "initialMetadata": {
                    "title": {
                        "newTitle": title
                    },
                    "description": {
                        "newDescription": description,
                        "shouldSegment": True
                    },
                    "privacy": {
                        "newPrivacy": privacy
                    },
                    "draftState": {
                        "isDraft": draft
                    }
                },
                "context": {
                    "client": {
                        "clientName": 62,
                        "clientVersion": "1.20201130.03.00",
                        "hl": "en-GB",
                        "gl": "PL",
                        "experimentsToken": "",
                        "utcOffsetMinutes": 60
                    },
                    "request": {
                        "returnLogEntry": True,
                        "internalExperimentFlags": [],
                        "sessionInfo": {
                            "token": self.session_token
                        }
                    },
                    "user": {
                        "delegationContext": {
                            "roleType": {
                                "channelRoleType": "CREATOR_CHANNEL_ROLE_TYPE_OWNER"
                            },
                            "externalChannelId": self.config['CHANNEL_ID']
                        },
                        "serializedDelegationContext": "",
                        "onBehalfOfUser": "",
                    },
                    "clientScreenNonce": ""
                },
                "delegationContext": {
                    "roleType": {
                        "channelRoleType": "CREATOR_CHANNEL_ROLE_TYPE_OWNER"
                    },
                    "externalChannelId": self.config['CHANNEL_ID']
                }
            }
        )

        return await upload.json()

    async def deleteVideo(self, video_id):
        delete = await self.session.post(
            f"https://studio.youtube.com/youtubei/v1/video/delete?alt=json&key={self.config['INNERTUBE_API_KEY']}",
            json={
                "videoId": video_id,
                "context": {
                    "client": {
                        "clientName": 62,
                        "clientVersion": "1.20201130.03.00",
                        "hl": "en-GB",
                        "gl": "PL",
                        "experimentsToken": "",
                        "utcOffsetMinutes": 60
                    },
                    "request": {
                        "returnLogEntry": True,
                        "internalExperimentFlags": [],
                        "sessionInfo": {
                            "token": ""
                        }
                    },
                    "user": {
                        "delegationContext": {
                            "roleType": {
                                "channelRoleType": "CREATOR_CHANNEL_ROLE_TYPE_OWNER"
                            },
                            "externalChannelId": self.config['CHANNEL_ID']
                        },
                        "serializedDelegationContext": ""
                    },
                    "clientScreenNonce": ""
                },
                "delegationContext": {
                    "roleType": {
                        "channelRoleType": "CREATOR_CHANNEL_ROLE_TYPE_OWNER"
                    },
                    "externalChannelId": self.config['CHANNEL_ID']
                }
            }
        )

        return await delete.json()
