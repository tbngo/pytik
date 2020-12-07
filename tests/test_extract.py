from pytik import extract
from pytik import TikTok


def test_description_with_class():
    tk = TikTok("https://www.tiktok.com/@tiktok/video/6881450806688664838")
    assert (
        tk.description()
        == "Good vibes only 🤙 @420doggface208 @mickfleetwood @tomhayes603"
    )


def test_user_with_class():
    tk = TikTok("https://www.tiktok.com/@tiktok/video/6881450806688664838")
    assert tk.user() == "tiktok"


def test_song_with_class():
    tk = TikTok("https://www.tiktok.com/@tiktok/video/6881450806688664838")
    assert tk.song() == "original sound"


def test_song_author_with_class():
    tk = TikTok("https://www.tiktok.com/@tiktok/video/6881450806688664838")
    assert tk.song_author() == "TikTok"


def test_nickname_with_class():
    tk = TikTok("https://www.tiktok.com/@tiktok/video/6881450806688664838")
    assert tk.nickname() == "TikTok"
