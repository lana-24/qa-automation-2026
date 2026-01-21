import requests
import pytest
from utils.helpers import method_post, method_get, method_put, method_patch, method_delete
from typing import Optional,Any
import jsonschema

def json_schema(data: dict[str, Any],schema_name: str):
    schemas = {
        "search" : {"type" : "object",
                    "properties" : {"id" : {"type" : "string"},
                                    "url" : {"type" : "string"},
                                    "width" : {"type" : "integer"},
                                    "height" : {"type" : "integer"},
                                    "mime_type" : {"type" : "string"}},
                    "required" : ["id","url"]
                    },
        
        "upload" : {"type" : "object",
                    "properties" : {"id" : {"type" : "string"},
                                    "url" : {"type" : "string"},
                                    "width" : {"type" : "integer"},
                                    "height" : {"type" : "integer"},
                                    "original_filename" : {"type" : "string"},
                                    "approved" : {"type" : "string"}
                                    },
                    "required" : ["id","url" ,"original_filename"]
                    },
        "list_upload" : {"type" : "array",
                         "items" : {
                             "type" : "object",
                             "properties" : {"id" : {"type": "string"},
                                             "url" : {"type": "string"},
                                             "width" : {"type": ["integer","null"]},
                                             "height" : {"type":["integer","null"]},
                                             "mime_type" : {"type": "string"}
                                             },
                             "required" : ["id","url",]}
                         },
        "analysis" : {"type" : "array",
                         "items" : {
                             "type" : "object",
                             "properties" : {"image_id" : {"type": "string"},
                                             "created_at" : {"type": "string"},
                                             "vendor" : {"type": "string"},
                                             
                                             },
                             "required" : ["image_id","created_at"]     
                         }
                }
        
    }

    schema = schemas.get(schema_name)
    jsonschema.validate(data, schema)
    
def test_images_search(headers):
    '''
    TC: P-IMAGES-01
    Search random images without token
    Endpoint: get /images/search
    Expected:
    - Status code 200
    - response body type object
    - response body field['id'->string,'url'->string,'mime_type'->string]
    '''
    
    response = method_get(endpoint='/images/search',headers=headers)
    assert response.status_code == 200 ,f'not 200 but {response.status_code}'
    json_schema(response.json(),'search')
    
def test_images_search_with_token(headers_token):
    '''
    TC: P-IMAGES-02
    Search random images with token
    Endpoint: get /images/search
    Expected:
    - status code 200
    - response body type object
    - response body field['id','url','mime_type']
    '''
    response = method_get(endpoint='/images/search',headers=headers_token)
    assert response.status_code == 200 ,f'not 200 but {response.status_code}'
    json_schema(response.json(),'search')

def test_images_upload(url,headers_token):
    '''
    TC: P-IMAGES-03
    Upload image cat
    Endpoint: post /images/upload
    Expected:
    - status code 201
    - response body type object
    - response body field['id','url','original_filename']
    '''
    files = {'file': ('images.jpeg', open('images.jpeg', 'rb'))}
    response = method_post(endpoint='/images/upload', headers=headers_token, files=files)
    assert response.status_code == 201 ,f'not 200 but {response.status_code}'
    json_schema(response.json(),'upload')
    # now delete
    image_id = response.json().get('id')
    rm =requests.delete(f'{url}/images/{image_id}')
    assert rm.status_code == 200 ,f'not 200 but {response.status_code}'
     
def test_images_myupload(headers_token):
    '''
    TC: P-IMAGES-04
    get my images 
    Endpoint: get /images/
    Expected:
    - status code 200
    - response body type array
    - response body field['id','url','created_at']
    '''
    response = method_get(endpoint='/images/',headers=headers_token)
    assert response.status_code == 200 ,f'not 200 but {response.status_code}'
    json_schema(response.json(),'list_upload')

def test_analysis_myupload(headers_token,get_id):
    '''
    TC: P-IMAGES-05
    Analysis my image
    Endpoint: get /images/{image_id}/analysis
    Expected:
    - status code 200
    - response body type object
    - response body field['image_id','created_at']
    '''
    response = method_get(endpoint= f'/images/{get_id}/analysis', headers=headers_token)
    assert response.status_code == 200 ,f'not 200 but {response.status_code}'
    json_schema(response.json(),'analysis')
    
def test_upload_images_breeds(headers_token,get_id):
    '''
    #TC: P-IMAGES-06
    Upload my image breeds
    Endpoint: post /images/{image_id}/breeds
    Expected:
    - status code 200
    - response body type object
    - response body field 'breeds_id'

    
    '''
    response = method_post(endpoint= f'/images/{get_id}/breeds',headers=headers_token)
    
    assert response.status_code == 200 ,f'not 200 but {response.status_code}'
    assert 'breed_id' in response.json()

def test_get_images_breeds(headers_token,get_id):
    '''
    TC: P-IMAGES-07
    Get my image breeds
    Endpoint: get /images/{image_id}/breeds
    Expected:
    - status code 200
    - response body type object
    - response body field 'breeds_id'
    '''
    response = method_post(endpoint= f'/images/{get_id}/breeds',headers=headers_token)
    assert response.status_code == 200 ,f'not 200 but {response.status_code}'
    assert 'breed_id' in response.json()

def test_delete_images_breeds(headers_token,get_id):
    '''
    TC: P-IMAGES-08
    Delete my image breeds
    Endpoint: delete /images/{image_id}/breeds/{breed_id}
    Expected:
    - status code 200
    - response body type object
    - response body field 'breeds_id'
    '''
    response = method_get(endpoint= f'/images/{get_id}/breeds',headers=headers_token)
    assert response.status_code == 200 ,f'not 200 but {response.status_code}'
    assert 'breed_id' in response.json()
    
def test_delete_myupload(headers_token,get_id):
    '''
    TC: P-IMAGES-09
    Delete my upload
    Endpoint: delete /images/{images_id}
    Expected:
    - status code 200
    '''
    response = method_delete(endpoint= f'/images/{get_id}/breeds', headers=headers_token)
    assert response.status_code == 200
