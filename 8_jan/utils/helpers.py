import requests

def make_requests(method ,url ,token=None ,data=None):
    headers = {
        "Accept" : "Application/vnd.github+json"
}

    if token:
        headers["Authorization"] = f'Bearer {token}'

    
    if method.upper() == 'GET':
        response = requests.get(url ,headers=headers)
        if response.status_code == 200:
            data = response.json()
            if isinstance(data, dict):
                return response
            else:
                print(f"response is'nt dict : {type(data)}")
                return response
        else:
            print(f'failed {response.status_code}')
            return response
            
    elif method.upper() == 'POST':
        response = requests.post(url ,headers=headers ,json=data)
        if isinstance(response.json(), dict):
            return response
        else:
            print("response is'nt dict")
    elif method.upper() == 'PUT' :
        response = requests.put(url, headers=headers ,json=data)
        if isinstance(response.json(), dict):
            return response
        else:
            print("response is'nt dict")
    elif method.upper() == 'PATCH':
        response = requests.patch(url, headers=headers ,json=data)
        if isinstance(response.json(), dict):
            return response
        else:
            print("response is'nt dict")
    elif method.upper() == 'DELETE':
        response = requests.delete(url, headers=headers)
        if isinstance(response.json(), dict):
            return response
        else:
            print("response is'nt dict")
    else:
        print('ada kesalahan')
