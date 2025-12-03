#real example

def api_call(response_code):
    if response_code > 0:
        if response_code==200:
            print("Request is successful")
        else:
            print("Error in the request")
    else:
        print("Response not send")
api_call(0)
api_call(404)
api_call(200)
api_call(response_code=503)   # calling the function using keyword response_code=
api_call(int(input("Enter the response code : ")))   #user input with int() function