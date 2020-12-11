from pytik import extract
from pytik import request
import re


class TikTok:
    """
    The core developer interface for pytik. pytik offloads the heavy lifting
    to smaller peripheral modules and functions.

    :param str url: The url of the TikTok video to gather data from
    """

    def __init__(self, url):
        self.url = url
        self.video_id = extract.video_id(url)
        self.html = None
        self.json = None  # Represents props json from the TikTok page's HTML after
        self.prefetch()

    def prefetch(self) -> None:
        """Eagerly download all necessary data.

        Eagerly executes all necessary network requests so all other
        operations don't does need to make calls outside of the interpreter
        which blocks for long periods of time.

        :rtype: None
        """
        self.html = request.get(url=self.url)
        self.json = extract.get_json(self.html)

    def description(self) -> str:
        """Returns the video's description

        :rtype: String
        """
        return extract.description(self.json)

    def user(self) -> str:
        """Returns the video's user

        :rtype: String
        """
        return extract.user(self.json)

    def nickname(self) -> str:
      """Returns the video creator's nickname

        :rtype: String
        """
        return extract.nickname(self.json)

    def song(self) -> str:
      """Returns the video's song

        :rtype: String
        """
        return extract.song(self.json)

    def song_author(self) -> str:
        """Returns the video's song author

        :rtype: String
        """
        return extract.song_author(self.json)
