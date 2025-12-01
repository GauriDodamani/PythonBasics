# An API sometimes fails due to network delays.
# Write a program to retry the API call 3 times until the response code becomes 200.
# If it still fails after 3 tries, print a failure message.   -> using if else too
# Hint: Use a while loop with a counter.
# Expected Output Example:
# Attempt 1: Response 500
# Attempt 2: Response 200
# ✅ Test Passed

response_code=int(input("Enter the response code : "))
api_call=3
counter=1

if response_code==200 or response_code==500:
    print("✅ Test Passed")
else:
    while counter<=api_call:
        print("Retry the API call")
        counter+=1


