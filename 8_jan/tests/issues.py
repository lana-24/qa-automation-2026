import requests
from configs.settings import GITHUB_TOKEN , URL
from utils.helpers import make_requests

base_url = URL
token = GITHUB_TOKEN

def print_response_body(data):
    if isinstance(data , dict):
        print('=' * 20 ,'RESPONSE BODY','='*20,'\n')
        print(f'id : {data['id']}')
        print(f'number : {data['number']}')
        print(f'state : {data['state']}')
        print(f'body : {data['body']}')
        print(f'login : {data['user']['login']}')
    elif isinstance(data , list):
        data1 = data[0]
        print('=' * 20 ,'RESPONSE BODY','='*20,'\n')
        print(f'id : {data1['id']}')
        print(f'number : {data1['number']}')
        print(f'state : {data1['state']}')
        print(f'body : {data1['body']}')
        print(f'user : {data1['user']['login']}')

    else:
        print('type is not dict or list')
        
def test_get_issues():
    '''
    TC-IS-01 : GET LIST ISSUES

    ENDPOINT : * GET /repos/{owner}/{repo}/issues
    EXPECTED :
    - status code 200
    - response body is list
    - response body field 'id'
    - response body field 'number'
    - response body field 'state'
    - response body field 'body'
    - response body field 'user[login]'
    '''
    url = f'{base_url}repos/octocat/Spoon-Knife/issues'
    try:
        response = make_requests('get', url )
        if response.status_code == 200:
            data = response.json()
            print_response_body(data)
        else:
            print(f'ada kesalahan : {response.status_code}')
    except Exception as e:
        print(f'ada kesalahan tak terduga {e}')
        
def test_get_issues_number():
    '''
    TC-IS-02 : GET ISSUES NUMBER

    ENDPOINT : * GET /repos/{owner}/{repo}/issues/{issue_number}
    EXPECTED :
    - status code 200
    - response body is dict
    - response body field 'id'
    - response body field 'number'
    - response body field 'state'
    - response body field 'body'
    - response body field 'user[login]'
    '''
    url = f'{base_url}repos/octocat/Spoon-Knife/issues/1'
    try:
        response = make_requests('get', url )
        if response.status_code == 200:
            data = response.json()
            print_response_body(data)
        else:
            print(f'ada kesalahan : {response.status_code}')
    except Exception as e:
        print(f'ada kesalahan tak terduga {e}')
        
def test_post_issues():
    '''
    TC-IS-03 : POST NEW ISSUES 

    ENDPOINT : * POST /repos/{owner}/{repo}/issues
    EXPECTED :
    - status code 201
    - response body is dict
    - response body field 'id'
    - response body field 'number'
    - response body field 'state'
    - response body field 'body'
    - response body field 'user[login]'
    '''
    url = f'{base_url}repos/lana-24/test-bikin-repository/issues'
    json = {
        "title" : "aku coba bikin issues dari requests",
        "body" : "apakah berhasil ?",
        "assignees" : ["lana-24"],
        "labels" : ["bug"]
}
    try:
        response = make_requests('post', url , token , json )
        if response.status_code == 201:
            data = response.json()
            print_response_body(data)
        else:
            print(f'ada kesalahan : {response.status_code}')
            print(f'response : {response.json()}')
    except Exception as e:
        print(f'ada kesalahan tak terduga {e}')
        
def test_patch_issues_number():
    '''
    TC-IS-04 : UPDATE ISSUES 

    ENDPOINT : * PATCH /repos/{owner}/{repo}/issues/{issue_number}
    EXPECTED :
    - status code 200
    - response body is dict
    - response body field 'id'
    - response body field 'number'
    - response body field 'state'
    - response body field 'body'
    - response body field 'user[login]'
    '''
    url = f'{base_url}repos/lana-24/test-bikin-repository/issues/3'
    json = {
        "title" : "aku coba ubah issues dari requests",
        "body" : "apakah berhasil ? yeyy berhasil ",
        "assignees" : ["lana-24"],
        "labels" : ["bug"]
}
    try:
        response = make_requests('patch', url , token , json )
        if response.status_code == 200:
            data = response.json()
            print_response_body(data)
        else:
            print(f'ada kesalahan : {response.status_code}')
            print(f'response : {response.json()}')
    except Exception as e:
        print(f'ada kesalahan tak terduga {e}')
        
def run_all():
    test_get_issues()
    test_get_issues_number()
    test_post_issues()
    test_patch_issues_number()
