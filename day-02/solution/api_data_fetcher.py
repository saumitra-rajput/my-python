import requests
import json

api_url = "https://jsonplaceholder.typicode.com/users" 

response = requests.get(url=api_url)

#first iterate list > then outof list iterate key,value of dict
print(type(response))
print(dir(response))
for i in response.json():
    for key,value in i.items():
        print(key,value)
    print("-----------")


data = [] # for storing processed data

# display only username and mail outof list 
print("\nList of User name and email\n")
for i in response.json():
    print(i["name"], i["email"])

    data.append({
        "name": i["name"],
        "email": i["email"]
        })

# print(data) # working fine

with open ("output.json", "w") as file:
    json.dump(data, file)
