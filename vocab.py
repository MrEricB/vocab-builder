import random

def convert_to_dict(in_file):
    dictionary = {}
    try:
        with open(in_file, 'r') as file:
            for line in file:
                if ':' in line:
                    key, value = map(str.strip, line.split(':', 1))
                    dictionary[key] = value
    except FileNotFoundError:
        print("Error: File not found")
    
    return dictionary

def get_random_word(dictionary):
    random_word = random.choice(list(dictionary.keys()))
    return random_word

def get_random_definition(dictionary):
    random_key = random.choice(list(dictionary.keys()))
    random_value = dictionary[random_key]
    return random_value
