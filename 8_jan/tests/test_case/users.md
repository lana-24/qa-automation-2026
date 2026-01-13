# Positive test

## TC-001: Get id user
**ID:** TC-USER-P-01  
**Priority:** High  
**Preconditions:** have user id

### Test Steps
1. Send GET request to `/user/{user_id}`
2. Capture response

### Expected Results
- Status code: 200
- Response body contains field `login`
- `id` field is integer > 0
- `followers and following ` >= 0


### Actual result 

### Status :  


## TC-002: Get users
**ID:** TC-USER-P-02  
**Priority:** MEDIUM  
**Preconditions:** 

### Test Steps
1. Send GET request to `/users`
2. Capture response

### Expected Results
- Status code: 200
- Response body contains field `login`


### Actual result 

### Status :  


## TC-003: Get users/{username}
**ID:** TC-USER-P-03  
**Priority:** HIGH  
**Preconditions:** know  username 

### Test Steps
1. Send GET request to `/users/{username}`
2. Capture response

### Expected Results
- Status code: 200
- Response body contains field `login`


### Actual result 

### Status :  

## TC-004: Get users followers
**ID:** TC-USER-P-04 
**Priority:** MEDIUM  
**Preconditions:** know username

### Test Steps
1. Send GET request to `/users/{username}/followers`
2. Capture response

### Expected Results
- Status code: 200


### Actual result 

### Status :  


## TC-005: Get users following
**ID:** TC-USER-P-05 
**Priority:** MEDIUM  
**Preconditions:** know username

### Test Steps
1. Send GET request to `/users/{username}/following`
2. Capture response

### Expected Results
- Status code: 200


### Actual result 

### Status :  

## TC-006: Get users social account
**ID:** TC-USER-P-06
**Priority:** MEDIUM  
**Preconditions:** know username

### Test Steps
1. Send GET request to `/users/{username}/social_accounts`
2. Capture response

### Expected Results
- Status code: 200


### Actual result 

### Status :  

