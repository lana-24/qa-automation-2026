import requests
from configs.config import BASE_URL

def api_requests(
        method,
        endpoint,
        headers=None,
        params=None,
        data=None,
        json_data=None,
        files=None
):
    """Helper untuk membuat request API"""
    url = f"{BASE_URL}/{endpoint}"
    
    response = requests.request(
        method=method,
        url=url,
        headers=headers or {},
        params=params or {},
        data=data,
        json=json_data
        files=files
    )
    
    # Return raw response untuk divalidasi oleh test case
    return response

# Atau function yang lebih spesifik
def requests_get(endpoint,headers=None, params=None):
    return api_requests('GET', endpoint, headers=headers, params=params)

def requests_post(endpoint,json_data,data=None ,files=None, headers=None):
    return api_requests('POST', endpoint, headers=headers, json_data=json_data ,data=None ,files=None)

def requests_put(endpoint, headers=None ,json_data):
    return api_requests('PUT', endpoint ,headers=headers ,json_data=json_data )

def requests_patch(endpoint, headers=None ,json_data):
    return api_requests('PATCH', endpoint ,headers=headers ,json_data=json_data)

def requests_delete(endpoint ,headers):
    return api_requests('DELETE',endpoint ,headers=headers)
