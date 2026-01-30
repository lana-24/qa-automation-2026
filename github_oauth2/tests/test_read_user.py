# scope read
import pytest
import os
import logging
from datetime import datetime
from utils.helpers import method_get, method_patch, method_delete ,method_post
from schemas.schema_user import user_schema

now = datetime.now().strftime("%d%b-%H-%M-%S-")
file = f"{os.path.basename(__file__).replace('.py', '')}--{now}.log"
logging.basicConfig(
    filename=file,
    level=logging.INFO,
    format='%(asctime)s | %(levelname)-8s | %(message)s',
    force=True
)
logger = logging.getLogger('SATPOL')

def logger_error(res, expect):
    if res.status_code != expect:
        logger.error(f'status code is {res.status_code}\nresponse:\n{res.json()}\n')

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
    logger_error(res, 200)
    assert res.status_code == 200
    user_schema(res.json(),'user')
    logger.info('<<END\n')
    
@pytest.mark.parametrize('account_id',
                         ['43339356',
                          '151425668',
                          '43920414',
                          '226660287'])
def test_get_user_id(headers_token,account_id):
    '''
    Test ID: TC-02
    Priority: HIGH
    Description: get a user with their id
    Expected: status 200 and type object
    '''
    logger.info(f'>>Starting get user{account_id} profile')
    endpoint = f'/user/{account_id}'
    res = method_get(endpoint, headers_token)
    logger_error(res, 200)
    assert res.status_code == 200
    user_schema(res.json(),'user')
    logger.info('<<END\n')
    
def test_get_list_user(headers_token):
    '''
    Test ID: TC-03
    Priority: HIGH
    Description: get list user
    Expected: status 200 and type array
    '''
    logger.info('>>Starting get a list user profile')
    endpoint = '/users'
    res = method_get(endpoint,headers_token)
    logger_error(res, 200)
    assert res.status_code == 200
    user_schema(res.json(),'users')
    logger.info('<<END\n')

@pytest.mark.parametrize("username",[
    "lana-24",
    "BR1LL14N",
    "deaafrizal",
    "ProgrammerZamanNow"
])
def test_get_user_by_username(headers_token, username):
    '''
    Test ID: TC-04 
    Priority: HIGH
    Description: get user with their username and get contexts
    Expected: status 200 and type object 
    '''
    endpoint = f'/users/{username}'
    logger.info(f'>>Starting get {username} profile')
    res = method_get(endpoint, headers_token)
    logger_error(res, 200)
    assert res.status_code == 200
    user_schema(res.json(), "user")
    logger.info('<<END\n')

def test_get_user_emails(headers_token):
    '''
    Test ID: TC-05
    Priority: MEDIUM
    Description: get list user emails or public emails
    Expected: status 200 and type array
    '''
    logger.info('>>Starting get list user emails')
    res = method_get('/user/public_emails', headers_token)
    logger_error(res, 200)
    assert res.status_code == 200,f'endpoint: /user/public_emails,response:\n{res.json()}'
    user_schema(res.json(),'list_email')
    logger.info('<<END\n')

def test_list_public_ssh_keys(headers_token):
    '''
    Test ID: TC-06
    Priority: HIGH
    Description: get list ssh public keys
    Expected: status 200 and type array
    '''
    logger.info('>>Starting get list ssh public keys')
    endpoint = '/user/keys'
    res = method_get(endpoint, headers_token)
    logger_error(res, 200)
    assert res.status_code == 200
    user_schema(res.json(),'list_ssh')
    logger.info('<<END\n')

def test_get_spesific_ssh_keys(headers_token,ssh_key):
    '''
    Test ID: TC-07
    Priority: HIGH
    Description: get spesific ssh public keys
    Expected: status 200 and type object
    '''
    logger.info('>>Starting get spesific ssh public keys')
    endpoint = f'/user/keys/{ssh_key}'
    res = method_get(endpoint, headers_token)
    logger_error(res, 200)
    assert res.status_code == 200
    user_schema(res.json(),'ssh')
    logger.info('<<END\n')

@pytest.mark.parametrize("username",[
    "lana-24",
    "defunkt",
    "deaafrizal",
    "BR1LL14N"
])
def test_public_keys_for_user(headers_token, username):
    '''
    Test ID: TC-08
    Priority: HIGH
    Description: get ssh public keys for a username
    Expected: status 200 and type array
    '''
    logger.info(f'>>Starting get {username} ssh public keys')
    endpoint = f'/users/{username}/keys'
    res = method_get(endpoint, headers_token)
    logger_error(res, 200)
    assert res.status_code == 200, f'username: {username}, response:\n{res.json()}'
    user_schema(res.json(),'public_ssh')
    logger.info('<<END\n')

'''=====NEGATIVE TEST====='''
def test_user_without_token():
    '''
    Test ID: TC-09
    Priority: HIGH
    Description: get /user, /user/emails,  user/keys, /user/keys/{key_id} 
    Expected: status 401 and get a error message 
    '''
    logger.info('>>Starting get a profile without token')
    endpoint = '/user'
    res = method_get(endpoint)
    logger_error(res, 401)
    assert res.status_code == 401
    logger.info(f'status code must be {res.status_code}')
    logger.info('<<END\n')

@pytest.mark.parametrize('account_id',[
    '433393871321',
    '1514256682312',
    '43920414214124',
    '226660232523587'])
def test_get_wrong_user_id(headers_token, account_id):
    '''
    Test ID: TC-10
    Priority: HIGH
    Description: get a wrong user id
    Expected: status 404 and get nothing 
    '''
    logger.info(f'>>Starting get wrong user id: {account_id}')
    endpoint = f'/user/{account_id}'
    res = method_get(endpoint, headers_token)
    logger_error(res, 404)
    assert res.status_code == 404
    logger.info(f'wrong id {account_id}')
    logger.info('<<END\n')

@pytest.mark.parametrize("username",[
    "lana-871",
    "bril14no",
    "deaalfariza",
    "progoromorjomonolde",
    "brilanone284"
])
def test_get_wrong_username(headers_token, username):
    '''
    Test ID: TC-11
    Priority: HIGH
    Description: get wrong username and the ssh keys
    Expected: status 404  
    '''
    logger.info(f'>>Starting get wrong username: {username}')
    endpoint = f'/user/{username}'
    res = method_get(endpoint, headers_token)
    logger_error(res, 404)
    assert res.status_code == 404
    logger.info(f'wrong username {username}')
    logger.info('<<END\n')
    
def test_patch_name_user(headers_token):
    '''
    Test ID: TC-12
    Priority: HIGH
    Description: edit new username with wrong scope
    Expected: status 404 
    '''
    logger.info('>>Starting edit new username,is it possible? ')
    endpoint = '/user'
    data = {"name" : "malikimut"}
    res = method_patch(endpoint, headers_token, json_data=data)
    logger_error(res, 404)
    assert res.status_code == 404
    logger.info('<<END\n')

def test_patch_email_visibility(headers_token):
    '''
    Test ID: TC-13
    Priority: HIGH
    Description: edit email visibility
    Expected: status 404
    '''
    logger.info('>>Starting edit email visibility')
    endpoint = '/user/email/visibility'
    data = {"visibility" : "private"}
    res = method_patch(endpoint, headers_token, json_data=data)
    logger_error(res, 404)
    assert res.status_code == 404
    logger.info('<<END\n')

def test_delete_email(headers_token):
    '''
    Test ID: TC-14
    Priority: HIGH
    Description: delete email
    Expected: status 404
    '''
    logger.info('>>Starting delete email ')
    endpoint = '/user/emails'
    email = {"emails" : ["maulmalikib@gmail.com"]}
    res = method_delete(endpoint, headers_token, json_data=email)
    logger_error(res, 404)
    assert res.status_code == 404
    logger.info('<<END\n')

def test_post_new_emails(headers_token):
    '''
    Test ID: TC-15
    Priority: HIGH
    Description: post new email 
    Expected: status 404
    '''
    logger.info('>>Starting post new emails   ')
    endpoint = '/user/emails'
    email = {"emails" : ["malikimut178b@gmail.com"]}
    res = method_post(endpoint, headers=headers_token, json_data=email)
    logger_error(res, 404)
    assert res.status_code == 404
    logger.info('<<END\n')
    
'''=====EDGE TEST====='''
@pytest.mark.parametrize("no", [101,
                                102,
                                200,
                                0,])
def test_get_101_list_user(headers_token, no):
    '''
    Test ID: TC-16 & 17
    Priority: LOW
    Description: get a user over the maximum or minimum
    Expected: status 200 and total 100 len  
    '''
    logger.info(f'>>Starting get {no} list user per page')
    endpoint = f'/users?per_page={no}'
    res = method_get(endpoint, headers_token)
    logger_error(res, 200)
    assert res.status_code == 200
    if no < 1:
        assert len(res.json()) == 30 #they said default 30
    else:
        assert len(res.json()) == 100 #they said 100 max
    logger.info('<<END\n')
