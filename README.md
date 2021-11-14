# Youtube Studio

Unofficial Async YouTube Studio API. Set of features limited or not provided by official YouTube API

> This is the Python version of [this project](https://github.com/adasq/youtube-studio). All thanks going to [@adasq](https://github.com/adasq) :)

## Installation

You can install with PIP.

`pip install ytstudio`

## Features

- Async
- Uploading Video (**NOT LIMITED** - official API's videos.insert charges you 1600 quota units)
- Deleting Video

## Examples

**Note:** You need cookies. Use an cookie manager([EditThisCookie](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg?hl=tr)) for needed cookies.

### Upload Video

> You need SESSION_TOKEN for upload video. [How to get Session Token?](https://github.com/adasq/youtube-studio#preparing-authentication)

```py
from ytstudio import Studio
import asyncio
import os

def progress(uploaded, total):
    print(f"{uploaded}/{total}", end="\r")
    pass

async def main():
    yt = Studio({'VISITOR_INFO1_LIVE': '', 'PREF': '', 'LOGIN_INFO': '', 'SID': '', '__Secure-3PSID': '', 'HSID': '', 'SSID': '', 'APISID': '', 'SAPISID': '', '__Secure-3PAPISID': '', 'YSC': '', 'SIDCC': ''})
    await yt.login()
    sonuc = await yt.uploadVideo(os.path.join(os.getcwd(), "deneme.mp4"), title="Hello World!", description="Uploaded by github.com/yusufusta/ytstudio",  progress=progress)
    print(sonuc['videoId']) # Print Video ID

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
```

## Author

Yusuf Usta, yusuf@usta.email

## Note

This library is in no way affiliated with YouTube or Google. Use at your own discretion. Do not spam with this.
