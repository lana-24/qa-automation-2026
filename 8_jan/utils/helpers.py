import requests

def make_requests(method ,url ,token=None ,data=None):
    headers = {
        "Accept" : "Application/json"
}

    if token:
        headers["Authorization"] = f'Bearer {token}'

    
    if method.upper() == 'GET':
        response = requests.get(url ,headers=headers)
        return response
    elif method.upper() == 'POST':
        response = requests.post(url ,headers=headers ,data=data)
        return response
    elif method.upper() == 'PUT' :
        response = requests.put(url, headers=headers ,data=data)
        return response
    elif method.upper() == 'PATCH':
        response = requests.patch(url, headers=headers ,data=data)
        return response
    elif method.upper() == 'DELETE':
        response = requests.delete(url, headers=headers)
        return response
    else:
        print('ada kesalahan')
