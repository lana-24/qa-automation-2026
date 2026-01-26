# Test Suite: GitHub User API

# Positive Test

## TC-001: Get Authenticated User
**ID:** TC-USER-P-01  
**Priority:** High  
**Preconditions:** Valid GitHub token

### Test Steps
1. Send GET request to `/user` with Authorization header
2. Capture response

### Expected Results
- Status code: 200
- Response body contains field `login`
- `id` field is integer > 0
- `followers and following ` >= 0


### Actual result (9-1-2025 4:39 PM)
- status code : 200
- response body contains field 'login'
- `id` field is integer > 0
- `followers and following ` >= 0

### Status : PASS 


## TC-001: Get spesific user
**ID:** TC-USER-P-02  
**Priority:** medium
**Preconditions:** no need token

### Test Steps
1. Send GET request to `/user/{username}`
2. capture response

### Expected Results
- Status code: 200
- Response body contains field `login`
- `id` field is integer > 0
- `followers and following ` >= 0


### Actual result (9-1-2025 4:39 PM)
- Status code: 200
- Response body contains field `login`
- `id` field is integer > 0
- `followers and following ` >= 0

### Status : PASS 


# Negative test

## TC-001: Get Authenticated User with invalid token
**ID:** TC-USER-N-001  
**Priority:** medium  
**Preconditions:** Invalid GitHub token

### Test Steps
1. Send GET request to `/user` with Authorization header
2. Capture response

### Expected Results
- Status code: 401


### Actual result (9-1-2025 4:39 PM) 
- Status code : 401 

### Status : PASS
