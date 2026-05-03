info = {
    "name": "Saumitra Rajput",
    "city": "Lucknow",
    "age": "I am God",
    "num": "22",
    "package": 3000000,
    "Role": "DevOps Engineer",
    "list": ["k8s", "docker", "GitHubActions"]
        }

print(f"I live {info["city"]}")
print("I am ", info["Role"])
print("I like to work with ",info.get("list"))

info.update({"dreamcompany": "Google"})

print(dir(info))

for key,value in info.items():
    print(key,value)
