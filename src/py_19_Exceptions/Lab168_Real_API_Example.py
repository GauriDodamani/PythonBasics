import requests

#response = requests.get("https://www.google.com")   # 200
#response = requests.get("http://www.gauriabc.com")     # ConnectionError

try:
    url = input("Enter the URL: ")
    response = requests.get(url,timeout=3)
    print(response.status_code)

except requests.exceptions.ConnectionError:
    print("Error due to wrong url input")

except requests.exceptions.Timeout:
    print("Taking too long")

except Exception as e:
    print(e)