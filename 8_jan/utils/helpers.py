import requests

def make_requests(method ,url ,token=None ,data=None ,params=None):
    headers = {
        "Accept" : "Application/vnd.github+json"
}

    if token:
        headers["Authorization"] = f'Bearer {token}'
        
    if params:
        try:
            response = requests.get(url ,headers=headers ,params=params,timeout=(3,10))
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
        except requests.exceptions.Timeout:
            print("Timeout ,check your connection!!")
        except reqeusts.exceptions.ConnectionError:
            print("connection error!!")

    if method.upper() == 'GET':
        try:
            response = requests.get(url ,headers=headers,timeout=(3,10))
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
        except requests.exceptions.Timeout :
            print('Timeout ,check your internet!!')
        except requests.exceptions.ConnectionError:
            print('Connection Error ,check you connection!!')
            
    elif method.upper() == 'POST':
        try:
            response = requests.post(url ,headers=headers ,json=data,timeout=(3,10))
            if isinstance(response.json(), dict):
                return response
            else:
                print("response is'nt dict")
        except requests.exceptions.Timeout :
            print('Timeout ,check your internet!!')
        except requests.exceptions.ConnectionError:
            print('Connection Error ,check you connection!!')
            
    elif method.upper() == 'PUT' :
        try:
            response = requests.put(url, headers=headers ,json=data,timeout=(3,10))
            if isinstance(response.json(), dict):
                return response
            else:
                print("response is'nt dict")
        except requests.exceptions.Timeout:
            print('Timeout ,check your internet!!')
        except reqeusts.exceptions.ConnectionError:
            print("connection error ")
            

    elif method.upper() == 'PATCH':
        try:
            response = requests.patch(url, headers=headers ,json=data,timeout=(3,10))
            if isinstance(response.json(), dict):
                return response
            else:
                print("response is'nt dict")
        except requests.exceptions.Timeout:
            print("Timeout , check you internet!!")
        except requests.exceptions.ConnectionError:
            print("connection error !!")
            
    elif method.upper() == 'DELETE':
        try:
            response = requests.delete(url, headers=headers,timeout=(3,10))
            if isinstance(response.json(), dict):
                return response
            else:
                print("response is'nt dict")
        except requests.exceptions.Timeout:
            print('Timeout ,check your internet')
        except requests.exceptions.ConnectionError:
            print("connection error!!")
    else:
        print('ada kesalahan')
