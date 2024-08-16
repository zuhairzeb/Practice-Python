# List of names
names = ["Adnan", "Hamza", "Ahmed", "Talha", "Haider"]

# Print each name with the message "is a student"
for name in names:
    print(f"{name} is a student")

# Use range to print numbers from 0 to 5
print("Numbers from range(6):")
for n in range(6):
    print(n)

# Use range to print numbers from 2 to 5
print("Numbers from range(2, 6):")
for x in range(2, 6):
    print(x)

# Use a while loop to print numbers from 0 to 5
print("Numbers from while loop (using j):")
i = 1
j = 0
while i <= 6:
    print(j)
    j += 1
    i += 1  # Increment i to avoid infinite loop

# Use a while loop to print numbers from 1 to 6
print("Numbers from while loop (using i):")
i = 1
while i <= 6:
    print(i)
    i += 1

# Use a while loop to print numbers from 1 to 2, then stop
print("Numbers from while loop with break:")
i = 1
while i <= 6:
    print(i)
    if i == 3:
        break
    i += 1
