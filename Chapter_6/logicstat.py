# Get the user's name and age
name = input("What is your name? ")
age = input("How old are you? ")

# Convert age to an integer for comparison
age = int(age)

# Check if the name contains only letters
if name.isalpha():
    print(f"Hello, {name}!")
else:
    print("The name should only contain letters.")

# Check if the age is a number and categorize the user
if age >= 18:
    if age > 60:
        print("You are a senior citizen.")
    else:
        print("You are an adult.")
else:
    print("You are not an adult.")

# Another way to categorize the user using 'elif'
if age < 18:
    print("You are a minor.")
elif age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")

# Using match-case (similar to switch) to categorize the user
match age:
    case 17:
        print(f"{name}, you are a minor.")
    case 40:
        print(f"{name}, you are an adult.")
    case 65:
        print(f"{name}, you are a senior citizen.")
    case _:
        print(f"{name}, you are in an undefined category.")

# More flexible match-case statement
match age:
    case _ if age < 18:
        print(f"{name}, you are a minor.")
    case _ if age < 60:
        print(f"{name}, you are an adult.")
    case _:
        print(f"{name}, you are a senior citizen.")
