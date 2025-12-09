'''
An API sometimes fails due to network delays.
Write a program to retry the API call 3 times until the response code becomes 200.
If it still fails after 3 tries, print a failure message.   -> using if else too
Hint: Use a while loop with a counter.

Expected Output Example:
Attempt 1: Response 500
Attempt 2: Response 200
✅ Test Passed
'''

#Logic build


#api_call=3
counter=1
while counter<=3:
    #print("Counter: ",counter)
    response_code = int(input("Enter the response code : "))
    print(f"Attempt {counter} : Response {response_code}")

    if response_code ==200:
        print("✅ Test Passed ")
        break
    else:
        counter += 1

if counter>3:
     print("API request Failed")



