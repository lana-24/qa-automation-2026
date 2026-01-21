# you can change the logic according the situation
import requests
import pytest
from configs.settings import base_url,token

@pytest.fixture
def headers_token():
    return { "Accept" : "application/json",
             "X-API-Key" : token }

@pytest.fixture
def headers():
    return { "Accept" : "application/json" }


@pytest.fixture
def url():
    return base_url

@pytest.fixture
def get_id(headers_token):
    files = {'file': ('images.jpeg', open('images.jpeg', 'rb'))}
    r = requests.post(f'{url}/images/upload',headers=headers_token ,files=files)
    assert r.status_code == 201
    img_id = r.json().get('id')

    yield img_id
    response = requests.get(f'{url}/images/{img_id}/analysis')
    if response.status_code != 404:
        rm = requests.delete(f'{url}/image/{img_id}')
        assert rm.status_code == 200
