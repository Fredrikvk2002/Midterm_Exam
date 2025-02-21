import random  # Import the random module to generate random numbers

# Create an empty list to store random numbers
random_numbers = []

# Generate 10 random numbers between 1 and 100 and add them to the list
for i in range(10):
    random_numbers.append(random.randint(1, 100))

# Print the original list of random numbers
print("Original list:", random_numbers)

# Loop through each index in the list
for i in range(len(random_numbers)):
    # If the number is greater than 50, replace it with a new random number between 20 and 30
    if random_numbers[i] > 50:
        random_numbers[i] = random.randint(20, 30)
    else:
        # If the number is 50 or less, replace it with "XX"
        random_numbers[i] = "XX"

# Print the modified list after replacements
print("Modified list:", random_numbers)

