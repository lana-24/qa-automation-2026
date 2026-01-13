from tests import authentication_user 

def run():
    print('menjalankan test user autheticated\n')
    authentication_user.test_user_authenticated()
    print('menjalankan test valid users\n')
    authentication_user.test_valid_users()
    print('menjalankan test invalid token\n')
    authentication_user.test_invalid_token()
    print('menjalankan test invalid user\n')
    authentication_user.test_invalid_users()
if __name__ == "__main__":
    run()
