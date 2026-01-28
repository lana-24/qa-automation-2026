from dotenv import load_dotenv
import os
import requests

load_dotenv()

"""
scope token :
- read:discussion,
- read:gpg_key,
- read:public_key,
- read:user
"""

token_oauth = os.getenv('token')
base_url = 'https://api.github.com/user'

def test_token():
    if token_oauth:
        headers ={
            "Accept" : "application/json",
            "Authorization" : f"Bearer {token_oauth}"
        }
        response = requests.get('https://api.github.com/user',headers=headers)
        if response.status_code == 200:
            print('token valid')
        else:
            print(f'response:\n{response.json()}')
    else:
        print('token kosong')
if __name__ == "__main__":
    test_token()


