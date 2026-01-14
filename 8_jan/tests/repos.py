from configs.settings import GITHUB_TOKEN, URL
from utils.helpers import make_requests

base_url = URL
token = GITHUB_TOKEN

def test_get_owner_repos():
    '''
    TC-RP-01 : GET OWNER REPOS

    METHOD : GET REPOS/{OWNER}/{REPO}
    EXPECTED:
    - RESPONSE STATUS 200
    - RESPONSE FIELD 'LOGIN' ,'ID', 'NAME'
    '''
    url = f'{base_url}/repos/BR1LL14N/porto'
    try:
        print(f"===== make requests {url} =====\n ")
        response = make_requests('get', url )
        print(f'response status : {response.status_code}')
        if response.status_code == 200:
            print('response :\n',response.json(),'\n')
        else:
            data = response.json()
            print('response : ')
            print(data['login'])
            print(data['fullname'])
            print(data['id'])
    except Exception as e:
        print(f'ada kesalahan {e}\n')
        
def test_get_repos_contents():
    '''
    TC-RP-02 : GET  REPOS CONTENTS

    METHOD : GET REPOS/{OWNER}/{REPO}/CONTENTS/{PATH}
    EXPECTED:
    - RESPONSE STATUS 200
    - RESPONSE FIELD 'LOGIN' ,'ID', 'NAME'
    '''
    url = f'{base_url}/BR1LL14N/porto/contents/css'
    try:
        print(f"===== make requests {url} =====\n ")
        response = make_requests('get', url )
        print(f'response status : {response.status_code}')
        if response.status_code == 200:
            data = response.json()
            print('response : ')
            print(data['login'])
            print(data['fullname'])
            print(data['id'])
        else:
            print(f'response status : {response.status_code} | expect 200\n ')
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
    url = f'{base_url}/users/BR1LL14N/repos'
    try:
        print(f"===== make requests {url} =====\n ")
        response = make_requests('get', url )
        print(f'response status : {response.status_code}')
        if response.status_code == 200:
            data = response.json()
            print('response : ')
            print(data['login'])
            print(data['fullname'])
            print(data['id'])
        else:
            print(f'response status : {response.status_code} | expect 200\n ')
    except Exception as e:
        print(f'ada kesalahan {e}\n')

def test_get_list_repos():
    '''
    TC-RP-04 : GET LIST REPOSITORY 

    EXPECTED:
    - RESPONSE STATUS 200
    - RESPONSE FIELD 'LOGIN' ,'ID', 'NAME'
    '''
    url=f'{base_url}/repositories'
    try:
        print(f"===== make requests {url} =====\n ")
        response = make_requests('get', url )
        print(f'response status : {response.status_code}')
        if response.status_code == 200:
            data = response.json()
            print('response : ')
            print(data['login'])
            print(data['fullname'])
            print(data['id'])
        else:
            print(f'response status : {response.status_code} | expect 200\n ')
    except Exception as e:
        print(f'ada kesalahan {e}\n')


def run_all():
    test_get_owner_repos()
    test_get_repos_contents()
    test_get_users_repos()
    test_get_list_repos()
