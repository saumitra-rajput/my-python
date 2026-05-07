# get the env from the user and print it

env = input("Enter the environment name: ") # taking input from the user

print("User has entered: ",env)

#  ==, != , >, <, >=, <=
# equal, not equalto, greaterthan, lessthan, greaterthanequalto, lessthanequalto

if env == "prod":
    print("Do not deploy on Friday!")
elif env == "stag":
    print("Take backup and test well")
else:
    print("All good, procced with the deployment: ", env)


a= int(input("Enter the first num: "))  # typecasting
b = int(input("Enter the second num: "))
c = int(input("Enter the third num: "))

print("The sum of a,b,c is: ", a+b+c)
