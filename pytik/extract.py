import requests
import json
import urllib.parse
import re


def video_id(url):
    """Extract the ``video_id`` from a TikTok url.
    This function supports the following patterns:
    - :samp:`https://www.tiktok.com/@{user}/video/{video_id}}`
    :param str url:
        A TikTok url containing a video id.
    :rtype: str
    :returns:
        TikTok video id.
    """
    return re.findall("\d+", url)[0]


def description(json):
    return json["props"]["pageProps"]["itemInfo"]["itemStruct"]["desc"]


def user(json):
    return json["props"]["pageProps"]["itemInfo"]["itemStruct"]["author"]["uniqueId"]


def nickname(json):
    return json["props"]["pageProps"]["itemInfo"]["itemStruct"]["author"]["nickname"]


def song(json):
    return json["props"]["pageProps"]["itemInfo"]["itemStruct"]["music"]["title"]


def song_author(json):
    return json["props"]["pageProps"]["itemInfo"]["itemStruct"]["music"]["authorName"]


def get_json(html):
    pattern = r"(?<={\"props\":)(.*?)(?=</script>)"
    regex = re.compile(pattern)
    result = regex.search(html)
    span = result.span()
    full_obj = '{"props":' + html[span[0] : span[1]]
    return json.loads(full_obj)
