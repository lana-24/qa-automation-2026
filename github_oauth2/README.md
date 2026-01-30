# HI THERE! WELCOME TO GITHUB OAUTH2

This folder contains scripts to obtain an access token from an authorization code and to test OAuth scopes.

### Authorization Code URL
Use the following link to get the authorization code:

https://github.com/login/oauth/authorize?client_id=Ov23liT4v0KIslLInnMI&scope=read:user,read:repo,read:public_key,read:gpg_key,read:discussion

---

## What is the difference from the `../github` folder?

In this folder, I started using the **pytest framework**, including:
- Fixtures
- Parametrization
- `pytest-html` for test reports
- Logging
- Error handling

Note: The generated token can only access **GET** requests and cannot be used for other HTTP methods.

---

## NOTES

- To see the **commit history**, switch to the `github_oauth` branch.
- To view the **test report** and logs without running the code, open the `report.html` file.
