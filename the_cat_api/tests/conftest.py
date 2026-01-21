# you can change the logic according the situation
import pytest
from configs.settings import base_url,token

@pytest.fixture
def headers_token():
    return { "Accept" : "application/json",
             "X-API-Key" : token }

@pytest.fixture
def url():
    return base_url
