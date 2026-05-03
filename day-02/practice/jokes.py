import requests

pj_url = "https://official-joke-api.appspot.com/random_joke"
random_jokes = "https://v2.jokeapi.dev/joke/Any?type=twopart"


def get_jokes(url_type,mood):
    try:
        headers = {
            "Accept": "application/json"
        }
    
        joke = requests.get(url=url_type,headers=headers)

        if mood == "pj":
            final_joke = joke.json()["setup"]+ joke.json()["punchline"]
    
        elif mood == "random":
            final_joke = joke.json()["setup"]+ joke.json()["delivery"]
        
        else:
            return "Invalid mood, Try pj or random."

        return final_joke
    
    except Exception as e:
        return f"Error occured: {e}"

mood = input("Enter the joke type eg. pj or random: ").lower()

if mood == "pj":
    url_type = pj_url 

elif mood == "random":
    url_type = random_jokes

else:
    url_type = random_jokes #fallback

final_joke = get_jokes(url_type,mood)

print(final_joke)



#response = requests.get(url=pj_url,headers=headers)
# print(response)
#joke = response.json()["setup"]+ response.json()["punchline"]
#print(joke)
# for key,value in response.json().items():
#     print(key,value)
