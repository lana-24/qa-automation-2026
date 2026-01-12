from tests import user_git

def run():
    print('menjalankan test user autheticated\n')
    user_git.test_user_authenticated()
    print('menjalankan test valid users\n')
    user_git.test_valid_users()
    print('menjalankan test invalid token\n')
    user_git.test_invalid_token()
    print('menjalankan test invalid user\n')
    user_git.test_invalid_users()
if __name__ == "__main__":
    run()
