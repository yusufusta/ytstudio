import pytest
import ytstudio
import json
import os

if os.path.exists("./login.json"):
    LOGIN_FILE = json.loads(open("./login.json", "r"))
else:
    exit("can't run test without login json")

studio = ytstudio.Studio(LOGIN_FILE)


@pytest.mark.asyncio
async def test_upload_video():
    await studio.login()
    assert 'videoId' in (await studio.uploadVideo(os.path.join(
        os.getcwd(), "test.mp4")))
