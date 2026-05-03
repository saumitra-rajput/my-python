import requests

url = "https://jsonplaceholder.typicode.com/todos/1" # server URL (API)

response = requests.get(url=url)

print(response)
print(type(response))

for key,value in response.json().items():
    print(key,value)
