from pytok import extract
from pytok import TikTok


def test_description_with_class():
    tk = TikTok("https://www.tiktok.com/@lilyachty/video/6842695315217190149?lang=en")
    assert tk.description() == "Motivational F R I D A Y 😂 #fyp #foryoupage"


def test_description():
    assert (
        extract.description(
            "https://www.tiktok.com/@lilyachty/video/6842695315217190149?lang=en"
        )
        == "Motivational F R I D A Y 😂 #fyp #foryoupage"
    )


def test_generate_driver():
    driver = extract.generate_driver(
        "https://www.tiktok.com/@lilyachty/video/6842695315217190149?lang=en"
    )
    assert driver != None


test_description()