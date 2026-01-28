# scope read
import pytest
import os
import logging
from datetime import datetime
from utils.helpers import method_get
from schemas.schema_user import user_schema

now = datetime.now().strftime("%d%b-%H:%M:%S:")
file = f"{os.path.basename(__file__).replace('.py', '')}--{now}.log"
logging.basicConfig(
    filename=file,
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-8s | %(message)s'
)
logger = logging.getlogger('SATPOL')


def test_read_profile(headers_token):
    '''
    Test ID: TC-01
    Priority: HIGH
    Description: get and read user profile
    Expected: status 200 and type object
    '''
    logger.info('>>Starting get user profile ')
    endpoint = '/user'
    res = method_get(endpoint,headers_token)
    if res.status_code != 200:
        logger.error(f'status code is {res.status_code}\nresponse:\n{res.json()}')
    assert res.status_code == 200
    user_schema(res.json(),'user')
    logger.info('<<END')
    
@pytest.mark.parametrize('account_id',[])
def test_get_user_id(account_id):
    '''
    Test ID: TC-02
    Priority: HIGH
    Description: get a user with their id
    Expected: status 200 and type object
    '''
    logger.info('>>Starting get user{id} profile')
    endpoint = f'/user/{account_id}'
    res = method_get(endpoint)
    if res.status_code != 200:
        logger.error(f'status code is {res.status_code}\nresponse:\n{res.json()}')
    assert res.status_code == 200
    user_schema(res.json(),'user')
    logger.info('<<END')
    
def test_get_list_user():
    '''
    Test ID: TC-03
    Priority: HIGH
    Descripton: get list user
    Expected: status 200 and type array
    '''
    logger.info('>>Starting get a list user profile')
    endpoint = '/users'
    res = method_get(endpoint)
    if res.status_code != 200:
        logger.error(f'status code is {res.status_code}\nresponse:\n{res.json()}')
    assert res.status_code == 200
    user_schema(res.json(),'users')
    logger.info('<<END')

@pytest.mark.parametrize("username, schema, ep",[
    ("lana-24", "user", None),
    ("lana-24", "hovecard", "ep"),
])
def test_get_user(username, schema, ep=None):
    '''
    Test ID: TC-04
    Priority: HIGH
    Description: get user with their username
    Expected: status 200 and type object 
    '''
    endpoint = f'/users/{username}'
    if ep:
        endpoint = f'/users/{username}/hovecard'
        logger.info(f'>>Starting get {username} hovecard')
    else:
        logger.info(f'>>Starting get {username} profile')
    res = method_get(endpoint)
    if res.status_code != 200:
        logger.error(f'status code is {res.status_code}\nresponse:\n{res.json()}')
    assert res.status_code == 200
    user_schema(res.json(), schema)
    logger.info('<<END')

def test_get_contextual_user():
    '''
    Test ID: TC-05
    Priority: HIGH
    Description: get contextual information for a user
    Expected: status 200 and type object containing a array
    '''
    logger.info('>>Starting get contexts user')
    endpoint = '/users/{username}/hovercard'
    logger.info('<<END')

def test_get_user_emails(headers_token):
    '''
    Test ID: TC-06
    Priority: MEDIUM
    Description: get list user emails
    Expected: status 200 and type array
    '''
    logger.info('>>Starting get list user emails')
    endpoint = '/user/emails'
    logger.info('<<END')

def test_list_public_email_user(headers_token):
    '''
    Test ID: TC-07
    Priority: MEDIUM
    Description: get list public emails user
    Expected: status 200 and type array
    '''
    logger.info('>>Starting get list public user emails')
    endpoint = '/user/public_emails'
    logger.info('<<END')

def test_list_public_ssh_keys(headers_token):
    '''
    Test ID: TC-08
    Priority: HIGH
    Description: get list ssh public keys
    Expected: status 200 and type array
    '''
    logger.info('>>Starting get list ssh public keys')
    endpoint = '/user/keys'
    logger.info('<<END')

def test_get_spesific_ssh_keys(headers_token):
    '''
    Test ID: TC-09
    Priority: HIGH
    Description: get spesific ssh public keys
    Expected: status 200 and type array
    '''
    logger.info('>>Starting get spesific ssh public keys')
    endpoint = '/user/keys/{key_id}'
    logger.info('<<END')

@pytest.mark.parametrize("username",[
    "lana-24",
    
])
def test_public_keys_for_user(username):
    '''
    Test ID: TC-10
    Priority: HIGH
    Description: get ssh public keys for a username
    Expected: status 200 and type array
    '''
    logger.info(f'>>Starting get {username} ssh public keys')
    endpoint = f'/users/{username}/keys'
    logger.info('<<END')

'''=====NEGATIVE TEST====='''
def test_user__without_token():
    '''
    Test ID: TC-11
    Priority: HIGH
    Description: get /user, /user/emails,  user/keys, /user/keys/{key_id} 
    Expected: status 401 and get a error message 
    '''
    logger.info('>>Starting get a profile without token')
    endpoint = '/user'
    logger.info('<<END')

@pytest.mark.parametrize()
def test_get_wrong_user_id(id):
    '''
    Test ID: TC-12
    Priority: HIGH
    Description: get a wrong user id
    Expected: status 404 and get nothing 
    '''
    logger.info('>>Starting get wrong user id:',id)
    endpoint = f'/user/{id}'
    logger.info('<<END')

@pytest.mark.parametrize("username",[
    "lana-871",
    "bril14no",
    
])
def test_get_wrong_username(username):
    '''
    Test ID: TC-13
    Priority: HIGH
    Description: get wrong username and the ssh keys
    Expected: status 404  
    '''
    logger.info('>>Starting get wrong username:',username)
    endpoint = f'/user/{username}'
    logger.info('<<END')
    
def test_patch_name_user(headers_token):
    '''
    Test ID: TC-14
    Priority: HIGH
    Description: edit new username with wrong scope
    Expected: status 403 
    '''
    logger.info('>>Starting edit new username ')
    endpoint = '/user'
    logger.info('<<END')

def test_patch_email_visibility(headers_token):
    '''
    Test ID: TC-15
    Priority: HIGH
    Description: edit email visibility
    Expected: status 403 
    '''
    logger.info('>>Starting edit email visibility')
    endpoint = '/user'
    logger.info('<<END')

def test_delete_email(headers_token):
    '''
    Test ID: TC-16
    Priority: HIGH
    Description: delete email
    Expected: status 403 
    '''
    logger.info('>>Starting edit new username ')
    endpoint = '/user'
    logger.info('<<END')

def test_post_new_emails(headers_token):
    '''
    Test ID: TC-17
    Priority: HIGH
    Description: post new email 
    Expected: status 403 
    '''
    logger.info('>>Starting post new emails   ')
    endpoint = '/user'
    logger.info('<<END')
    
'''=====EDGE TEST====='''
def test_get_101_list_user():
    '''
    Test ID: TC-18
    Priority: LOW
    Description: get a profile without token
    Expected: status 200 and total 100 len  
    '''
    logger.info('>>Starting get 101 list user per page')
    endpoint = '/users?per_page=101'
    logger.info('<<END')

def test_get_0_list_user():
    '''
    Test ID: TC-19
    Priority: LOW
    Description: get a profile without token
    Expected: status 200  
    '''
    logger.info('>>Starting get 0 list user per page')
    endpoint = '/users?per_page=0'
    logger.info('<<END')
