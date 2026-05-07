# function = kam

# ek kam karo, 2 number input lo aur
# sum print kar do


def sum_of_num(): # defining the function
    num1 = int(input("Enter the num 1: "))
    num2 = int(input("Enter the num 2: "))
    sum = num1 + num2
    print(f"The sum of numbers is: {sum}")

# sum_of_num() # calling the function

env = input("Enter the environment name: ") # taking input from the user

print("User has entered: ",env)
if env == "prod":
    sum_of_num()
    print("Do not deploy on Friday!")
elif env == "stag":
    print("Take backup and test well")
else:
    print("All good, procced with the deployment: ", env)


def take_backup():
    print("Taking backup.....")

day = input("Enter the day: ")
if day == "monday":
    take_backup()
