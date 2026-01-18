from configs.settings import GITHUB_TOKEN, URL
from utils.helpers import make_requests
import jsonschema
from jsonschema import validate

base_url = URL
token = GITHUB_TOKEN

def validate_json(json):
    schema= {
        "type" : "object",
        "properties" : {
            "id" : {"type " : "integer"},
            "fullname" : {"type " : "string"},
            "name" : {"type " : "string"}
        },
        "required" : ["id"]
}
    try:
        validate(instance=json ,schema=schema)
        print("json is valid")
        print_response_body(json)
    except jsonschema.exceptions.ValidationError as e:
        print(f"gagal validasi :  {e}")

def print_response_body(json):
    if isinstance(json , dict):
        print('response : ')
        print('id :',json['id'])
        print('full name :',json['full_name'])
        print('name :',json['name'])
    elif isinstance(json , list):
        json1 = json[0]
        print('response : ')
        print('id :',json1['id'])
        print('full name :',json1['full_name'])
        print('name :',json1['name'])
        
def test_get_owner_repos():
    '''
    TC-RP-01 : GET OWNER REPOS

    METHOD : GET REPOS/{OWNER}/{REPO}
    EXPECTED:
    - RESPONSE STATUS 200
    - RESPONSE FIELD 'LOGIN' ,'ID', 'NAME'
    '''
    url = f'{base_url}repos/BR1LL14N/porto'
    try:
        print(f"===== make requests {url} =====\n ")
        response = make_requests('get', url )
        if response.status_code == 200:
            print(f'response status : {response.status_code}')
            data = response.json()
            validate_json(data)
        else:
            print(f'response status : {response.status_code} | expect 200')
            print('response :\n',response.json(),'\n')
    except Exception as e:
        print(f'ada kesalahan \n{e}\n')
        
def test_get_repos_contents():
    '''
    TC-RP-02 : GET  REPOS CONTENTS

    METHOD : GET REPOS/{OWNER}/{REPO}/CONTENTS/{PATH}
    EXPECTED:
    - RESPONSE STATUS 200
    - RESPONSE FIELD 'LOGIN' ,'ID', 'NAME'
    '''
    url = f'{base_url}repos/BR1LL14N/porto/contents/css'
    try:
        print(f"===== make requests {url} =====\n ")
        response = make_requests('get', url )
        if response.status_code == 200 and response is not None:
            print(f'response status : {response.status_code}')
            data = response.json()
            data1 = data[0]
            print('response : ')
            print(f'type : {data1['type']}')
            print(f'path : {data1['path']}')
            print(f'name : {data1['name']}')
            print(f'size : {data1['size']}')
        else:
            print(f'response status : {response.status_code} | expect 200\n ')
            print(type(response))
            
    except Exception as e:
        print(f'ada kesalahan {e}\n')
        
def test_get_users_repos():
    '''
    TC-RP-03 : GET USERS REPOS

    METHOD : GET USERS/{USERNAME}/REPOS
    EXPECTED:
    - RESPONSE STATUS 200
    - RESPONSE FIELD 'LOGIN' ,'ID', 'NAME'
    '''
    url = f'{base_url}users/BR1LL14N/repos'
    try:
        print(f"===== make requests {url} =====\n ")
        response = make_requests('get', url )
        if response.status_code == 200:
            print(f'response status : {response.status_code}')
            data = response.json()
            data1 = data[0]
            validate_json(data1)
        else:
            print(f'response status : {response.status_code} | expect 200\n ')
            print('response :\n',response.json  ,'\n')
    except Exception as e:
        print(f'ada kesalahan {e}\n')

def test_get_list_repos():
    '''
    TC-RP-04 : GET LIST REPOSITORY 

    EXPECTED:
    - RESPONSE STATUS 200
    - RESPONSE FIELD 'LOGIN' ,'ID', 'NAME'
    '''
    url=f'{base_url}repositories'
    try:
        print(f"===== make requests {url} =====\n ")
        response = make_requests('get', url )
        if response.status_code == 200:
            print(f'response status : {response.status_code}')
            data = response.json()
            data1= data[0]
            validate_json(data1)
        else:
            print(f'response status : {response.status_code} | expect 200\n ')
            print('response :\n',response.json(),'\n')
    except Exception as e:
        print(f'ada kesalahan {e}\n')
        #print(f'response : /n{response.json()}')


def run_all():
    test_get_owner_repos()
    test_get_repos_contents()
    test_get_users_repos()
    test_get_list_repos()
