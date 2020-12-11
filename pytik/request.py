import re
from urllib import parse
from urllib.request import Request
from urllib.request import urlopen
import ssl


def _execute_request(url):
    base_headers = {"User-Agent": "Mozilla/5.0", "accept-language": "en-US,en"}
    if url.lower().startswith("http"):
        request = Request(url, headers=base_headers)
    else:
        raise ValueError("Invalid URL")
    return urlopen(request, context=ssl.SSLContext())


def get(url):
    """Send an http GET request.

    :param str url:
        The URL to perform the GET request for.
    :rtype: str
    :returns:
        UTF-8 encoded string of response
    """
    return _execute_request(url).read().decode("utf-8")
