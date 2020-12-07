from pytik import extract
from pytik import request
import re


class TikTok:
    def __init__(self, url):
        self.url = url
        self.video_id = extract.video_id(url)
        self.html = None
        self.json = None  # Represents props json in from the TikTok page's HTML
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
        return extract.description(self.json)

    def user(self) -> str:
        return extract.user(self.json)

    def nickname(self) -> str:
        return extract.nickname(self.json)

    def song(self) -> str:
        return extract.song(self.json)

    def song_author(self) -> str:
        return extract.song_author(self.json)
