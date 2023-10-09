"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Mojmír Švábenský
email: Mojmir1@seznam.cz
discord: _bluecuracao
"""

'''
author =
'''
Text_1 = '''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30 and the Union Pacific Railroad,
which traverse the valley.'''


Text_2 = '''
At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.
'''

Text_3 = '''
The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.
'''

# Combine all texts into a dictionary
TEXTS = {'1': Text_1, '2': Text_2, '3': Text_3}

separator = "-" * 48

# User registration

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Function to authenticate a user
def authenticate_user(username, password):
    return username in users and users[username] == password

# Requesting username and password
def main():
    print("Welcome! Please enter your username and password to log in.")
    
    while True:
        print(separator)
        username = input("Username: ")
        print(separator)
        password = input("Password: ")
        print(separator)

        if authenticate_user(username, password):
            print("Login successful. Welcome, {}!".format(username))
            print("You have access to 3 texts for analysis.")
            break
        else:
            print("Invalid username or password. Exiting the program.")
            exit()  

if __name__ == "__main__":
    main()

# After successful login
selected_text = input("Select a text number (1, 2, 3) for analysis: ")
print(separator)

if selected_text in TEXTS:
    chosen_text = TEXTS[selected_text]
    words = chosen_text.split()
    word_count = len(words)
    print("Number of words in the selected text: ", word_count)

    # Number of words starting with a capital letter
    words_starting_with_capital = [word for word in words if word.istitle()]
    word_count_starting_with_capital = len(words_starting_with_capital)
    print("Number of words starting with a capital letter: ", word_count_starting_with_capital)

    # Number of words written in uppercase
    words_in_uppercase = [word for word in words if word.isupper()]
    word_count_in_uppercase = len(words_in_uppercase)
    print("Number of words written in uppercase: ", word_count_in_uppercase)

    # Number of words written in lowercase
    words_in_lowercase = [word for word in words if word.islower()]
    word_count_in_lowercase = len(words_in_lowercase)
    print("Number of words written in lowercase: ", word_count_in_lowercase)

    # Number of numbers in the selected text
    numbers = [word for word in words if word.isdigit()]
    number_count = len(numbers)
    print("Number of numbers in the selected text:", number_count)

    # Sum of all numbers (not digits) in the text
    sum_of_numbers = sum([int(number) for number in numbers])
    print("Sum of all numbers in the selected text:", sum_of_numbers) 
    print(separator)
else:
    print("You entered an invalid text choice or the text is not available. Exiting the program.")
    print(separator)

# Creating a dictionary with word length frequencies
word_lengths = [len(word) for word in words]
frequencies = {length: word_lengths.count(length) for length in set(word_lengths)}

# Sorting the dictionary by word lengths
frequencies = dict(sorted(frequencies.items()))

# Getting the maximum frequency for normalization
max_count = max(frequencies.values())

# Printing a bar chart to the console
print("LEN |     OCCURRENCES     |    NR")
print(separator)
for length, count in frequencies.items():
    # Normalizing the column length based on the maximum frequency
    column = "*" * int(20 * count / max_count)
    print(f"{length:2} | {column:20} | {count:2}")
