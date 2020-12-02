import extract


class TikTok:
    def __init__(self, url):
        self.url = url

    def description(self) -> str:
        return extract.description(self.url)

    def user(self) -> str:
        return extract.user(self.url)


tk = TikTok("https://www.tiktok.com/@chrissyvroom4/video/6900744385122585861?lang=en")
print(tk.user())
print(tk.description())