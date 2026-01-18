import requests
from configs.settings import GITHUB_TOKEN ,URL
from utils.helpers import make_requests
import jsonschema
from jsonschema import validate

base_url = URL
token = GITHUB_TOKEN

def json_validation(json):
    schema = {
        "type" : "object",
        "properties" : {"total_count" : {"type" : "integer"},
                        "incomplete_results" : {"type" : "boolean"}},
        "required" : ["total_count"]
}
    try:
        validate(instance=json , schema=schema)
        print("json is valid")
        print_response_body(json)
    except jsonschema.exceptions.ValidationError as e:
        print(f'error validation : \n {e}')

def print_response_body(data):
    print('='*20,'response body','='*20)
    print(f'total count : {data['total_count']}')
    print(f'incomplete_results : {data['incomplete_results']}\n')

def test_search_repo():
    '''
    TC-SC-01 : SEARCH PYTHON REPOSITORY

    METHOD : GET /SEARCH/{REPO}?q=Q
    EXPECTED :
    - RESPONSE STATUS 200
    - RESPONSE BODY TYPE IS DICT
    
    '''
    url = f'{base_url}search/repositories'
    params = {
        "q" : "python"
}
    try:
        response = make_requests('get',url ,params=params)
        if response.status_code == 200:
            data = response.json()
            json_validation(data)
        else:
            print(f'ada kesalahan {response.status_code }')
    except Exception as e:
        print(f'ada kesalahan tak terduga \n{e}')

def test_search_issues():
    '''
    TC-SC-02 : SEARCH BUG ISSUES 

    METHOD : GET /SEARCH/{ISSUES}?q=Q
    EXPECTED :
    - RESPONSE STATUS 200
    - RESPONSE BODY TYPE IS DICT
    
    '''
    url = f'{base_url}search/issues'
    params = {
        "q" : "bug"
}
    try:
        response = make_requests('get',url ,params=params)
        if response.status_code == 200:
            data = response.json()
            json_validation(data)
        else:
            print(f'ada kesalahan {response.status_code }')
    except Exception as e:
        print(f'ada kesalahan tak terduga \n{e}')

def test_search_code():
    '''
    TC-SC-03 : SEARCH CONSOLE.LOG CODE

    METHOD : GET /SEARCH/{CODE}?q=Q
    EXPECTED :
    - RESPONSE STATUS 200
    - RESPONSE BODY TYPE IS DICT
    
    '''
    url = f'{base_url}search/code'
    params = {
        "q" : "try+except+requests"
}
    try:
        response = make_requests('get',url ,token=token,params=params)
        if response.status_code == 200:
            data = response.json()
            print(f'status code : {response.status_code}')
            json_validation(data)
        else:
            print(f'ada kesalahan {response.status_code }')
    except Exception as e:
        print(f'ada kesalahan tak terduga \n{e}')

def run_all():
    test_search_repo()
    test_search_issues()
    test_search_code()
