import requests
import jsonschema
from jsonschema import validate

from configs import settings
from utils.helpers import make_requests

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
    print(f"id : {response['id']} | tipe data string")
    print(f"public repos : {response['public_repos']}")
    print(f"followers : {response['followers']}")
    print(f"following : {response['following']}")
    print(f"followers : {response['followers']} | bukan int")
    print(f"following : {response['following']} | bukan int")
    print(f"created at : {response['created_at']}\n")

    
'''Positive case'''
def test_user_authenticated(): # get user with authenticated
    url = f'{settings.URL}/user'
    response = make_requests('GET',url ,settings.GITHUB_TOKEN)
    
    data = response.json()
    print(f"status code : {response.status_code}")
    if response.status_code == 200:
        validate_json(data)
        return True
    
def test_valid_users(): # get spesific user without token 
    response = make_requests('get',f'{settings.URL}/users/BR1LL14N')
    data = response.json()
    print(f"status code : {response.status_code}")
    if response.status_code == 200:
        validate_json(data)

''' Negatif test'''


def test_invalid_token():
    token = f"Bearer {settings.GITHUB_TOKEN}salah",

    response = make_requests('get',f'{settings.URL}' , token)
    data = response.json()
    print(f"status code : {response.status_code}")
    print(data, "\n")

def test_invalid_users():
    url_users = f'{settings.URL}/users/lana-871'
    response = make_requests("get", url_users)
    data = response.json()
    if response.status_code == 404:
        print(f'url : {url_users} tidak di termukan ')
    print(f"status code : {response.status_code}")
    print(f'body : {data}')

def run_all():
    test_user_authenticated()
    test_valid_users()
    print('='*20,'NEGATIVE TEST','='*20)
    test_invalid_token()
    test_invalid_users()
