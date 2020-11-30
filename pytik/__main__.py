from pytik import extract


class TikTok:
    def __init__(self, url):
        self.url = url

    def description(self) -> str:
        return extract.description(self.url)
