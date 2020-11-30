from pytok import extract
from pytok import TikTok


def test_description():
    tk = TikTok("https://www.tiktok.com/@lilyachty/video/6842695315217190149?lang=en")
    assert tk.description() == "Motivational F R I D A Y 😂 #fyp #foryoupage"


test_description()