from ytstudio import Studio
import asyncio
import json
import os

if os.path.exists("./login.json"):
    LOGIN_FILE = json.loads(open("./login.json", "r"))
else:
    exit("can't run example without login json")
yt = Studio(LOGIN_FILE)


async def edit_video():
    await yt.login()
    sonuc = await yt.editVideo(
        video_id="aaaaaaaa",
        title="test",  # new title
        description="test",  # new description
        privacy="PUBLIC",  # new privacy status (PUBLIC, PRIVATE, UNLISTER)
        tags=["test", "test2"],  # new tags
        category=22,  # new category
        thumb="./test.png",  # new thumbnail (png, jpg, jpeg, <2MB)
        playlist=["aaaaa", "bbbbbb"],  # new playlist
        monetization=True,  # new monetization status (True, False)
    )
    print(f"successfully edited! videoId: {sonuc['videoId']}")


async def delete_video():
    await yt.login()
    sonuc = await yt.deleteVideo(
        video_id="aaaaaaaa",
    )
    print(f"successfully deleted! videoId: {sonuc['videoId']}")

loop = asyncio.get_event_loop()
loop.run_until_complete(edit_video())
loop.run_until_complete(delete_video())
