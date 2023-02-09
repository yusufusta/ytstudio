from ytstudio import Studio
import asyncio
import json
import os


async def get_video_list():
    if os.path.exists("./login.json"):
        LOGIN_FILE = json.loads(open("./login.json", "r").read())
    else:
        exit("can't run example without login json")

    yt = Studio(LOGIN_FILE)

    await yt.login()
    sonuc = await yt.listVideos()
    print(sonuc)


async def get_video():
    if os.path.exists("./login.json"):
        LOGIN_FILE = json.loads(open("./login.json", "r"))
    else:
        exit("can't run example without login json")

    yt = Studio(LOGIN_FILE)

    await yt.login()
    sonuc = await yt.getVideo("aaaaaaa")
    print(sonuc)

loop = asyncio.get_event_loop()
loop.run_until_complete(get_video())
loop.run_until_complete(get_video_list())
