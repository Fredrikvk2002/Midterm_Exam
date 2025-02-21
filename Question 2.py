def is_palindrome(number):
    return str(number) == str(number)[::-1]

# List of numbers from the question
numbers = [
    "5485839837501070045005400701057389385845",
    "7489617719749244646336564429479177169847",
    "6593036601359343374664733439531066303956",
    "8025833559061079503003059701609553385208"
]

# Check which one is NOT a palindrome
for number in numbers:
    if not is_palindrome(number):
        print(f"{number} is NOT a palindrome")
