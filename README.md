# pytik
![GitHub](https://img.shields.io/github/license/thengo1/pytik)
![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/thengo1/pytik/tests/main)
![Codecov](https://img.shields.io/codecov/c/github/thengo1/pytik)
![Read the Docs](https://img.shields.io/readthedocs/pytik)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

pytik is a Python library for gathering metadata from a TikTok video.

## Installation

```bash
$ python -m pip install pytik
```

## Getting Started

pytik exposes a TikTok class, enabling you to request specific attributes from a TikTok video.

```python
 >>> from pytik import TikTok
 >>> tk = TikTok('https://www.tiktok.com/@gordonramsayofficial/video/6898822706662231302?lang=en')
 >>> tk.description()
 >>> tk.user()
```
