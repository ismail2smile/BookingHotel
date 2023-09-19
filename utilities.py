import random
import string

def generate_random_string(length):
    # Define the characters you want to include in the random string
    characters = string.ascii_letters + string.digits  # You can add more characters if needed

    # Use random.choices to generate a random string of the specified length
    random_string = ''.join(random.choices(characters, k=length))

    return random_string

def generate_random_number(length):
    # Define the characters as digits
    characters = string.digits  # Only digits (0-9)

    # Use random.choices to generate a random string of the specified length
    random_string = ''.join(random.choices(characters, k=length))

    return random_string