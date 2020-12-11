import json
import urllib.parse
import re


def video_id(url):
    """Extract the ``video_id`` from a TikTok url.
    This function supports the following patterns:
    - :samp:`https://www.tiktok.com/@{user}/video/{video_id}`

    :param str url:
        A TikTok url containing a video id.
    :rtype: str
    :returns:
        TikTok video id.
    """
    return re.findall(r"\d+", url)[0]


def description(json):
    """Extract the description from a TikTok url.

    :param json json:
        Parsed JSON of the TikTok video's HTML page.
    :rtype: str
    :returns:
        TikTok description.
    """
    return json["props"]["pageProps"]["itemInfo"]["itemStruct"]["desc"]


def user(json):
    """Extract the user from a TikTok url.

    :param json json:
        Parsed JSON of the TikTok video's HTML page.
    :rtype: str
    :returns:
        TikTok user.
    """
    return json["props"]["pageProps"]["itemInfo"]["itemStruct"]["author"]["uniqueId"]


def nickname(json):
    """Extract the nickname of the user from a TikTok url.

    :param json json:
        Parsed JSON of the TikTok video's HTML page.
    :rtype: str
    :returns:
        TikTok user's nickname.
    """
    return json["props"]["pageProps"]["itemInfo"]["itemStruct"]["author"]["nickname"]


def song(json):
    """Extract the song from a TikTok url.

    :param json json:
        Parsed JSON of the TikTok video's HTML page.
    :rtype: str
    :returns:
        TikTok song.
    """
    return json["props"]["pageProps"]["itemInfo"]["itemStruct"]["music"]["title"]


def song_author(json):
    """Extract the song's author from a TikTok url.

    :param json json:
        Parsed JSON of the TikTok video's HTML page.
    :rtype: str
    :returns:
        TikTok song author.
    """
    return json["props"]["pageProps"]["itemInfo"]["itemStruct"]["music"]["authorName"]


def get_json(html):
    """Use regex to parse a TikTok page's HTML code to get 'props' JSON data

    :param str html:
        Full HTML code of a TikTok page
    :rtype: json
    :returns:
        JSON object of 'props'
    """
    pattern = r"(?<={\"props\":)(.*?)(?=</script>)"
    regex = re.compile(pattern)
    result = regex.search(html)
    span = result.span()
    full_obj = '{"props":' + html[span[0] : span[1]]
    return json.loads(full_obj)
