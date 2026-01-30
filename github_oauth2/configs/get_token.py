from dotenv import load_dotenv, set_key
import os
import requests

load_dotenv()

client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')
uri = os.getenv('uri')
code = os.getenv('code')

data = {
    "client_id" : client_id.strip(),
    "client_secret" : client_secret.strip(),
    "code" : code.strip()
    #redirect_uri" : uri
}
headers = {
    "Accept" : "application/json"
}
response = requests.post('https://github.com/login/oauth/access_token',headers=headers, data=data, timeout=5)

print(f'response :\n{response.json()}')
env_file = '.env'
if response.status_code == 200:
    data  = response.json()
    token = data['access_token']
    set_key(env_file ,'token', token)
