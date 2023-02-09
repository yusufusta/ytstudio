from ytstudio import Studio
import asyncio
import os
import json
import datetime


def progress(yuklenen, toplam):
    print(f"{round(yuklenen / toplam) * 100}% upload", end="\r")
    pass


if os.path.exists("./login.json"):
    LOGIN_FILE = json.loads(open("./login.json", "r").read())
else:
    exit("can't run example without login json")

yt = Studio(LOGIN_FILE)


async def main():
    await yt.login()
    up_result, edit_result = await yt.scheduledUploadVideo(os.path.join(os.getcwd(), "test_video.mp4"), progress=progress, schedule_time=datetime.datetime.now() + datetime.timedelta(minutes=30), scheduled_privacy="PUBLIC", )
    print(f"successfully uploaded! videoId: {up_result['videoId']}")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
