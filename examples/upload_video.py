from ytstudio import Studio
import asyncio
from pyquery import PyQuery as pq
import os


def progress(yuklenen, toplam):
    #print(f"{yuklenen}/{toplam}", end="\r")
    pass


async def main():
    yt = Studio({'VISITOR_INFO1_LIVE': '', 'PREF': '', 'LOGIN_INFO': '', 'SID': '', '__Secure-3PSID': '', 'HSID': '',
                'SSID': '', 'APISID': '', 'SAPISID': '', '__Secure-3PAPISID': '', 'YSC': '', 'SIDCC': ''}, session_token="")
    await yt.login()
    sonuc = await yt.uploadVideo(os.path.join(os.getcwd(), "deneme.mp4"), progress=progress)
    print(sonuc['videoId'])

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
