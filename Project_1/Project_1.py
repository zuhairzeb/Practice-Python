while True:
    # name
    name = input("Please enter your name: ")  
    
    # Validate the name input
    if not name.isalpha():
        print("Error: Name should only contain letters.")
        continue  
    
    # age
    age_input = input("Please enter your age: ")

    # Validate the age input
    if not age_input.isdigit():
        print("Error: Age should be a number.")
        continue  

    # Convert the age input to an integer
    age = int(age_input)

    if age >= 18:
        print(f"{name}, you are considered an adult.")
    else:
        print(f"{name}, you are not yet an adult.")

    # Break out 
    break
