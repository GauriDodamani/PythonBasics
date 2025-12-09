# Write a Function to Check Test Case Status
# Problem:
# Write a function check_status(status_code) that returns:
# "PASS" if status_code = 200
# "FAIL" if status_code = 400 or 500
# "UNKNOWN" otherwise
# Example Input & Output:
# print(check_status(200))   # PASS
# print(check_status(500))   # FAIL
# print(check_status(302))   # UNKNOWN


#defining the function

def check_status(status_code) :
    match status_code :
        case 200 :
            return "PASS"
        case 400 :
            return "FAIL"
        case 500:
            return "FAIL"
        case _ :
            return "UNKNOWN"

#User input
code=int(input("Enter the status code : "))

#calling the function
result = check_status(code)
print(result)

