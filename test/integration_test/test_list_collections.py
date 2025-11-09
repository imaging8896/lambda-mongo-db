import pytest

from datetime import datetime, timedelta

from db import list_collections


def test_get_latest_dividend_announcement():
    list_collections("stage")
