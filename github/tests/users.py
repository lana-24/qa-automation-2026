import requests
from configs import settings
from utils.helpers import make_requests
import jsonschema
from jsonschema import validate

def validate_json(json):
    schema = {
        "type" : "object",
        "properties" : {
            "id" : {"type" : "integer"},
            "public_repos" : {"type" : "integer"},
            "followers" : {"type" : "integer"},
            "following" : {"type" : "integer"},
            "created_at" : {"type" : "string"}
        },
        "required" : ["id", "public_repos"]
}  
    try:
        validate(instance=json ,schema=schema)
        print('json data is valid\n')
        print_github_profile(json)
        
    except jsonschema.exceptions.ValidationError as e:
        print(f'json data is invalid : {e}')

def print_github_profile(response):
    print("===== PROFIL GITHUB =====" )
    print(f"username : {response['login']}")
    print(f"id : {response['id']} ")
    print(f"public repos : {response['public_repos']}")
    print(f"followers : {response['followers']}")
    print(f"following : {response['following']}")
    print(f"created at : {response['created_at']}\n")

'''positive test'''

def test_get_id_user():
    url = f'{settings.URL}user/226660287' #lana-24
    print(f'starting get {url} \n ')
    try:
        response = make_requests('get', url )
        if response.status_code == 200:
            print(f'status code : {response.status_code} ')
            validate_json(response.json())
        else:
            print(f'status code : {response.status_code} | expected 200 ')
    except Exception as e:
        print(f'ada kesalahan \n{e} ')

def test_get_users(): # btw ini hanya 1 page ,jumlah nya 30
    url = f'{settings.URL}users'
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
    url = f'{settings.URL}users/lana-24'
    try:
        response = make_requests('get', url )
        if response.status_code == 200:
            print(f'status code : {response.status_code} ')
            validate_json(response.json())
        else:
            print(f'status code : {response.status_code} | expected 200 ')
    except Exception as e:
        print(f'ada kesalahan \n{e} ')

def test_get_users_followers():
    url = f'{settings.URL}users/lana-24/followers'
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
    url = f'{settings.URL}users/lana-24/following'
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
    url = f'{settings.URL}users/lana-24/social_accounts'
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

    
