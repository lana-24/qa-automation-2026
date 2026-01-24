# you can change the logic according the situation
import requests
import pytest
from configs.settings import base_url,token
from pathlib import Path

@pytest.fixture
def headers_token():
    return { "Accept" : "application/json",
             "x-api-key" : token }

@pytest.fixture
def headers():
    return { "Accept" : "application/json" }


@pytest.fixture
def url():
    return base_url

@pytest.fixture
def get_id(headers_token,images,url):
    files = {'file': ('images.jpg', images, 'image/jpeg')}
    r = requests.post(f'{url}/images/upload',headers=headers_token ,files=files)
    assert r.status_code == 201 ,f'make id error not 201 but {r.status_code}, response:\n{r.text}'
    img_id = r.json().get('id')
    assert r.json().get('approved') == 1

    yield img_id
    rget = requests.get(f'{url}/images/{img_id}')
    if rget.status_code == 200:
        rm = requests.delete(f'{url}/images/{img_id}',headers=headers_token)
        assert rm.status_code == 204,f'get id error not 204 but {rm.status_code}, response:\n{rm.text}'

@pytest.fixture
def images():
    image_path = Path(__file__).parent / 'images.jpeg'
    with open(image_path, 'rb') as f:
        yield f



def pytest_html_results_table_header(cells):
    # Di versi baru, 'items' diganti 'cells'
    cells.insert(2, "<th>Description</th>")

def pytest_html_results_table_row(report, cells):
    # Mengambil deskripsi yang kita simpan di objek report
    description = getattr(report, "description", "")
    cells.insert(2, f"<td>{description}</td>")

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    # Mengambil docstring dari fungsi test
    doc = item.function.__doc__
    report.description = str(doc) if doc else ""
