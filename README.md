![GitHub](https://img.shields.io/github/license/thengo1/pytok)

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
