import pytest
from py.xml import html
from configs.settings import token_oauth

def parse_docstring(docstring):
    if not docstring:
        return {}
    
    data = {}
    lines = docstring.strip().split('\n')
    
    for line in lines:
        line = line.strip()
        if ':' in line:
            key, value = line.split(':', 1)
            data[key.strip()] = value.strip()
    
    return data

def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Test ID'))
    cells.insert(3, html.th('Priority'))
    cells.insert(4, html.th('Description'))
    cells.insert(5, html.th('Expected'))

def pytest_html_results_table_row(report, cells):
    test_id = getattr(report, 'test_id', '-')
    priority = getattr(report, 'priority', '-')
    description = getattr(report, 'description', '-')
    expected = getattr(report, 'expected', '-')
    
    cells.insert(2, html.td(test_id))
    cells.insert(3, html.td(priority))
    cells.insert(4, html.td(description))
    cells.insert(5, html.td(expected))

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    
    docstring = item.function.__doc__
    
    if docstring:
        parsed = parse_docstring(docstring)
        
        report.test_id = parsed.get('Test ID', '-')
        report.priority = parsed.get('Priority', '-')
        report.description = parsed.get('Description', '-')
        report.expected = parsed.get('Expected', '-')
        
    else:
        report.test_id = '-'
        report.priority = '-'
        report.description = 'No description'


@pytest.fixture()
def headers_token():
    return {
        "Accept" : "application/json",
        "Authorization" : token_oauth
}

@pytest.fixture()
def headers():
    return  {"Accept" : "application/json"}

