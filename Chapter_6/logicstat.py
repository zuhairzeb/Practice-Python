# Get user input
name = input("What is your name? ")
age = input("How old are you? ")

# Check if the name is valid
if name.isalpha():
    print(f"Hello, {name}!")
else:
    print("Invalid name. Please enter letters only.")

# Check if age is a number
if age.isdigit():
    age = int(age)  # Convert age to integer
    
    # Determine the age category
    if age < 18:
        print("You are a minor.")
    elif age < 60:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")
else:
    print("Invalid age. Please enter a number.")
