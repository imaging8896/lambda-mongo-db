import os

import pytest


@pytest.fixture
def database_name():
    return os.environ["TEST_MONGO_DB_NAME"]
