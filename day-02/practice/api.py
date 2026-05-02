import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1" # server URL (API)

response = requests.get(url=api_url)

for key,value in response.json().items():
    print(key,value)
    if key == "userId":
        if value in [100,200,300]:
            print("User found")



import requests

api_url = api_url

response = requests.get(url=api_url)

for key,value in response.json().items():
    print(key,value)

    if key == "userID":
        if value in [200,100,300]:
            print("User found")
