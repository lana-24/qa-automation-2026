import requests
from configs.settings import URL,GITHUB_TOKEN

base_url = f'{URL}rate_limit'
token = GITHUB_TOKEN
def rate_limit_without_token():
    try:
        response = requests.get(base_url)
        if response.status_code == 200:
            data = response.json()
            print(f'limit : {data["resources"]["core"]["limit"]}')
            print(f'remaining : {data["resources"]["core"]["remaining"]}\n')
        else:
            print(f'ada kesalahan {response.status_code}\n')
    except Exception as e:
        print(f'ada kesalahan tak terduga {e}')

def rate_limit_with_token():
    try:
        response = requests.get(base_url , headers={"Authorization" : f"Bearer {token}"})
        if response.status_code == 200:
            data = response.json()
            print('====== with token =====')
            print(f'limit : {data["resources"]["core"]["limit"]}')
            print(f'remaining : {data["resources"]["core"]["remaining"]}')
        else:
            print(f'ada kesalahan {response.status_code}')
    except Exception as e:
        print(f'ada kesalahan tak terduga\n {e}')

def run_all():
    rate_limit_without_token()
    rate_limit_with_token()
