# Youtube Studio

Unofficial Async YouTube Studio API. Set of features limited or not provided by official YouTube API!

> This is the Python version of [this project](https://github.com/adasq/youtube-studio). All thanks going to [@adasq](https://github.com/adasq) :)

## Installation

You can install with [PIP](https://pypi.org/project/ytstudio/).

`pip install ytstudio`

## Features

Look at the documentation: [Click here](https://yusufusta.github.io/ytstudio/)

- Fully Async
- [Uploading Video](https://yusufusta.github.io/ytstudio/#ytstudio.Studio.uploadVideo) - [Example](https://github.com/yusufusta/ytstudio/blob/master/examples/upload_video.py) (**NOT LIMITED** - official API's videos.insert charges you 1600 quota units)
- [Deleting Video](https://yusufusta.github.io/ytstudio/#ytstudio.Studio.deleteVideo) - [Example](https://github.com/yusufusta/ytstudio/blob/master/examples/edit_video.py#L29)
- [Edit Video](https://yusufusta.github.io/ytstudio/#ytstudio.Studio.editVideo) - [Example](https://github.com/yusufusta/ytstudio/blob/master/examples/edit_video.py#L13)
- [Get Video(s)](https://yusufusta.github.io/ytstudio/#ytstudio.Studio.listVideos) - [Example](https://github.com/yusufusta/ytstudio/blob/master/examples/get_videos.py#L7)

## Login

You need cookies for login. Use an cookie manager([EditThisCookie](https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg?hl=tr)) for [needed cookies.](https://github.com/yusufusta/ytstudio/blob/master/examples/login.json)

Also you need SESSION_TOKEN for (upload/edit/delete) video. [How to get Session Token?](https://github.com/adasq/youtube-studio#preparing-authentication)

## TO-DO

- [ ] Better Documentation
- [ ] Better Tests
- [ ] More Functions

## Author

Yusuf Usta, yusuf@usta.email

## Note

This library is in no way affiliated with YouTube or Google. Use at your own discretion. Do not spam with this.
