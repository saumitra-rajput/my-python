# For loop

for i in range(5):
    print("Hello World!")

# simple table using loop
num = int(input("For Loop Enter the number : "))
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}") # using f = formatting

# simple usage of while loop

# num = int(input("Enter the number: "))

#while num == 4:
#    print("JAI hooo") # example of infinite loop
#    break



choice = input("Enter the q to exit: ")
while choice != "q":
    num = int(input("Enter the number: "))

    for i in range(1, 11):
        print(f"{num} x {i} = {num*i}")
    choice = input("Enter the q to exit or enter to continue: ")
