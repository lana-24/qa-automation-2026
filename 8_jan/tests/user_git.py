
import requests

from configs import settings 
'''Positive case'''
def test_user_authenticated(): # get user with authenticated
    headers = {
        "Authorization" : f"Bearer {settings.GITHUB_TOKEN}",
        "Accept" : "application/json"
    }
    # Tambah try-except untuk network errors
    try:
        responses = requests.get(settings.URL , headers=headers)
        responses.raise_for_status()  # Auto raise untuk 4xx/5xx
    except requests.exceptions.RequestException as e:
        print(f"❌ Request failed: {e}")
        return

    response = responses.json()
    print(f"status code : {responses.status_code}")
    assert "login" in response , "tidak ada field login"
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

def test_valid_users(): # get spesific user without token
    url_users = f'{settings.URL}s/lana-24'

    headers = {
         "Accept" : "application/json"
    }

    responses = requests.get(url_users , headers=headers)
    response = responses.json()
    print(f"status code : {responses.status_code}")
    assert "login" in response , "tidak ada field login"
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

''' Negatif test'''
def test_invalid_token():
    headers = {
        "Authorization" : f"Bearer {settings.GITHUB_TOKEN}salah",
        "Accepts" : "application/json"
    }

    responses = requests.get(settings.URL , headers=headers)
    response = responses.json()
    print(f"status code : {responses.status_code}")
    print(response, "\n")

def test_invalid_users():
    url_users = f'{settings.URL}s/lana-871'

    headers = {
         "Accept" : "application/json"
    }

    responses = requests.get(url_users , headers=headers)
    response = responses.json()
    if responses.status_code == 404:
        print(f'url : {url_users} tidak di termukan ')
    print(f"status code : {responses.status_code}")
    print(f'body : {response}')
