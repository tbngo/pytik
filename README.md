# pytik
![License](https://img.shields.io/github/license/thengo1/pytik?color=gree)
![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/thengo1/pytik/tests/main)
[![Codecov](https://img.shields.io/codecov/c/github/thengo1/pytik)](https://codecov.io/gh/thengo1/pytik)
[![Docs](https://img.shields.io/readthedocs/volga.svg)](https://pytik.readthedocs.io)
[![PyPI](https://img.shields.io/pypi/v/pytik?color=gree)](https://pypi.org/project/pytik/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

pytik is a lightweight, dependency-free Python library for fetching data from TikTok.

## Installation

```bash
$ pip install pytik
```

## Getting Started

pytik exposes a TikTok class, enabling you to request specific attributes from a TikTok video.

```python
 >>> from pytik import TikTok
 >>> tk = TikTok('https://www.tiktok.com/@tiktok/video/6881450806688664838')
 >>> tk.description()
 "Good vibes only 🤙 @420doggface208 @mickfleetwood @tomhayes603"
 >>> tk.user()
 "tiktok"
 >>> tk.song()
 "original sound"
 >>> tk.song_author() 
 "TikTok"
```
