try:
    data= open("test.json").read()

except FileNotFoundError as fnfe:           #fnfe:-- FileNotFoundError
    print(fnfe)