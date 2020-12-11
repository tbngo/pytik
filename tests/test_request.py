from pytik import request
from pytik import TikTok
import pytest


def test_get_invalid_url():
    with pytest.raises(ValueError):
        request.get("a bad url")
