
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

    
'''Positive case'''
def test_user_authenticated(): # get user with authenticated
    responses = make_requests('GET',settings.URL ,settings.GITHUB_TOKEN)
    
    response = responses.json()
    print(f"status code : {responses.status_code}")
    if responses.status_code == 200:
        print_github_profile(response)
        return True
    
def test_valid_users(): # get spesific user without token 
    responses = make_requests('get',f'{settings.URL}s/lana-24')
    response = responses.json()
    print(f"status code : {responses.status_code}")
    if responses.status_code == 200:
        print_github_profile(response)

''' Negatif test'''
def test_invalid_token():
    token = f"Bearer {settings.GITHUB_TOKEN}salah",

    responses = make_requests('get',settings.URL , token)
    response = responses.json()
    print(f"status code : {responses.status_code}")
    print(response, "\n")

def test_invalid_users():
    url_users = f'{settings.URL}s/lana-871'
    responses = make_requests("get", url_users)
    response = responses.json()
    if responses.status_code == 404:
        print(f'url : {url_users} tidak di termukan ')
    print(f"status code : {responses.status_code}")
    print(f'body : {response}')
