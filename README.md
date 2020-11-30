![GitHub](https://img.shields.io/github/license/thengo1/pytok)
[![codecov](https://codecov.io/gh/thengo1/pytok/branch/main/graph/badge.svg?token=9W25J9UEIR)](https://codecov.io/gh/thengo1/pytok)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# pytok
pytok is a lightweight Python library for gathering metadata from a TikTok video.

## Installation
```bash
$ python -m pip install pytok
```

## Getting Started
pytok exposes a TikTok class, enabling you to request specific attributes from a TikTok video.

```python
 >>> from pytok import TikTok
 >>> tk = TikTok('https://www.tiktok.com/@gordonramsayofficial/video/6898822706662231302?lang=en')
 >>> tk.description()
 >>> tk.user()
```
