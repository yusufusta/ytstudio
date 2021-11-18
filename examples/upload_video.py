from ytstudio import Studio
import asyncio
import os
import json


def progress(yuklenen, toplam):
    print(f"{round(yuklenen / toplam) * 100}% upload", end="\r")
    pass


if os.path.exists("./login.json"):
    LOGIN_FILE = json.loads(open("./login.json", "r"))
else:
    exit("can't run example without login json")

yt = Studio(LOGIN_FILE)


async def main():
    await yt.login()
    sonuc = await yt.uploadVideo(os.path.join(os.getcwd(), "test_video.mp4"), progress=progress)
    print(f"successfully uploaded! videoId: {sonuc['videoId']}")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
