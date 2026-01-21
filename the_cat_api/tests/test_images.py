from utils.helpers import requests_post ,requests_get ,requests_put, reqeusts_patch ,requests_delete

def json_schema(schema_name):
    schemas = {
        "search" : {"type" : "object",
                    "properties" : {"id" : {"type" : "string"},
                                    "url" : {"type" : "string"},
                                    "width" : {"type" : "integer"},
                                    "height" : {"type" : "integer"},
                                    "mime_type" : {"type" : "string"}}
                    "required" : ["id","url"]
                    },
        "upload" : {"type" : "object",
                    "properties" : {"id" : {"type" : "string"},
                                    "url" : {"type" : "string"},
                                    "width" : {"type" : "integer"},
                                    "height" : {"type" : "integer"},
                                    "original_filename" : {"type" : "string"},
                                    "approved" : {"type" : "string"}
                                   }
                    "required" : ["id","url" ,"original_filename"]
                    },
        "list_upload" : {"type" : "array",
                         "items" : {
                             "type" : "object",
                             "properties" : {"id" : {"type" : "string"},
                                             "url" : {"type" : "string"},
                                             "width" : {"type" : "integer"},
                                             "height" : {"type" : "integer"},
                                             "mime_type" : {"type" : "string"},
                                             "created_at" : {"type" : "string"}}
                             "required" : ["id","url","created_at"]     
                         }
                         }
        
    }

    schema = schemas.get(schema_name)
    jsonschema.validate(data, schema)
    
def test_images_search(url):
    '''
    TC: P-IMAGES-01
    Search random images without token
    Endpoint: get /images/search
    Expected:
    - Status code 200
    - response body type object
    - response body field['id'->string,'url'->string,'mime_type'->string]
    '''

def test_images_search_with_token(url ,headers_token):
    '''
    TC: P-IMAGES-02
    Search random images with token
    Endpoint: get /images/search
    Expected:
    - status code 200
    - response body type object
    - response body field['id','url','mime_type']
    '''

def test_images_upload(url ,headers_token):
    '''
    TC: P-IMAGES-03
    Upload image cat
    Endpoint: post /images/upload
    Expected:
    - status code 201
    - response body type object
    - response body field['id','url','original_filename']
    '''
    files = {'file': ('kucingku.jpg', open('kucingku.jpg', 'rb'))}
    # Requests akan handle closing-nya

def test_image_myupload(url ,headers_token):
    '''
    TC: P-IMAGES-04
    get my images 
    Endpoint: get /images/
    Expected:
    - status code 200
    - response body type array
    - response body field['id','url','created_at']
    '''

def test_analysis_myupload(url,headers_token):
    '''
    TC: P-IMAGES-05
    Analysis my image
    Endpoint: get /images/{image_id}/analysis
    Expected:
    - status code 200
    - response body type object
    - response body field['image_id','created_at']
    '''

def test_upload_images_breeds(url,headers_token):
    '''
    TC: P-IMAGES-06
    Upload my image breeds
    Endpoint: post /images/{image_id}/breeds
    Expected:
    - status code 200
    - response body type object
    - response body field 'breeds_id'
    '''

def test_get_images_breeds(url,headers_token):
    '''
    TC: P-IMAGES-07
    Get my image breeds
    Endpoint: get /images/{image_id}/breeds
    Expected:
    - status code 200
    - response body type object
    - response body field 'breeds_id'
    '''

def test_delete_images_breeds(url,headers_token):
    '''
    TC: P-IMAGES-08
    Delete my image breeds
    Endpoint: delete /images/{image_id}/breeds
    Expected:
    - status code 200
    - response body type object
    - response body field 'breeds_id'
    '''
    
def test_delete_myupload(url ,headers_token):
    '''
    TC: P-IMAGES-09
    Delete my upload
    Endpoint: delete /images/{images_id}
    Expected:
    - status code 200
    '''
