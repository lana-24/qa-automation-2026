import requests
from configs import settings
from utils.helpers import make_requests

def print_github_profile(response):
    print("===== PROFIL GITHUB =====" )
    print(f"username : {response['login']}")
    if isinstance(response['id'], int):
        print(f"id : {response['id']} ")
    else:
        print(f"id : {response['id']} | tipe data string")
    print(f"public repos : {response['public_repos']}")
    if isinstance(response['followers'],int) and isinstance(response['following'],int):
        print(f"followers : {response['followers']}")
        print(f"following : {response['following']}")
    else:
        print(f"followers : {response['followers']} | bukan int")
        print(f"following : {response['following']} | bukan int")

    print(f"created at : {response['created_at']}\n")

'''positive test'''

def test_get_id_user():
    url = f'{settings.URL}/226660287' #lana-24
    print(f'starting get {url} \n ')
    try:
        response = make_requests('get', url )
        if response.status_code == 200:
            print(f'status code : {response.status_code} ')
            print_github_profile(response.json())
        else:
            print(f'status code : {response.status_code} | expected 200 ')
    except Exception as e:
        print(f'ada kesalahan \n{e} ')

def test_get_users():
    url = f'{settings.URL}s'
    print(f'starting get {url} \n ')
    try:
        response = make_requests('get', url )
        if response.status_code == 200:
            print(f'status code : {response.status_code} ')
            print('total : ',len(response.json()),'\n')
        else:
            print(f'status code : {response.status_code} | expected 200 ')
    except Exception as e:
        print(f'ada kesalahan \n{e} ')

def test_get_user_username():
    url = f'{settings.URL}s/lana-24'
    try:
        response = make_requests('get', url )
        if response.status_code == 200:
            print(f'status code : {response.status_code} ')
            print_github_profile(response.json())
        else:
            print(f'status code : {response.status_code} | expected 200 ')
    except Exception as e:
        print(f'ada kesalahan \n{e} ')

def test_get_users_followers():
    url = f'{settings.URL}s/lana-24/followers'
    print(f'\nstarting get {url} \n ')
    try:
        response = make_requests('get', url )
        if response.status_code == 200:
            print(f'status code : {response.status_code} ')
            print('response : ',response.json())
        else:
            print(f'status code : {response.status_code} | expected 200 ')
            print(f'response :\n {response.json()}')
    except Exception as e:
        print(f'ada kesalahan \n{e} ')

def test_get_users_following():
    url = f'{settings.URL}s/lana-24/following'
    print(f'\nstarting get {url} \n ')
    try:
        response = make_requests('get', url )
        if 'login ' in response.json():
            print(f'status code : {response.status_code} ')
            print('response :',response.text)
        else:
            print(f'response :\n {response.json()}')
    except Exception as e:
        print(f'ada kesalahan \n{e} ')

def test_get_users_socialaccounts():
    url = f'{settings.URL}s/lana-24/social_accounts'
    print(f'starting get {url} \n ')
    try:
        response = make_requests('get', url )
        if response.status_code == 200:
            print(f'status code : {response.status_code} ')
            print('response :', response.json())
        else:
            print(f'status code : {response.status_code} | expected 200 ')
            print(f'response :\n {response.json()}')
    except Exception as e:
        print(f'ada kesalahan \n{e} ')


def run_all():
    test_get_id_user()
    test_get_users()
    test_get_user_username()
    test_get_users_followers()
    test_get_users_following()
    test_get_users_socialaccounts()

    
