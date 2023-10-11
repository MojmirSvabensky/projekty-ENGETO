"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Mojmír Švábenský
email: Mojmir1@seznam.cz
discord: _bluecuracao
"""

# Combine all texts into a dictionary
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.''',
]

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
def login():
    print("Welcome! Please enter your username and password to log in.")    
    while True:
        print(separator)
        username = input("Username: ")
        print(separator)
        password = input("Password: ")
        print(separator)
        if authenticate_user(username, password):
            print("Login successful. Welcome, {}!".format(username))                 
            return username        
        else:
            print("Invalid username or password. Exiting the program.")
            exit()
              
# Function to analyze text
def analyze_text(selected_text):
    if selected_text.isdigit() and 1 <= int(selected_text) <= len(TEXTS):
        index = int(selected_text) - 1
        chosen_text = TEXTS[index]
        words = chosen_text.split()
        word_count = len(words)
        word_lengths = [len(word.strip('.,!?')) for word in words]
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
        print("Invalid input. Please enter an integer between 1 and {}. Terminating the program.".format(len(TEXTS)))
        quit()

def frequency(selected_text):
    if selected_text.isdigit() and 1 <= int(selected_text) <= len(TEXTS):
        index = int(selected_text) - 1
        chosen_text = TEXTS[index]
        words = chosen_text.split()
        
        # Create a dictionary to count word length frequencies
        word_length_counts = {}
        for word in words:
            word_length = len(word.strip('.,!?'))
            if word_length in word_length_counts:
                word_length_counts[word_length] += 1
            else:
                word_length_counts[word_length] = 1

        # Determine the maximum word length
        max_word_length = max(word_length_counts.keys())

        # Print the frequency table
        print("LEN |     OCCURRENCES     |    NR")
        print(separator)
        for length in range(1, max_word_length + 1):
            count = word_length_counts.get(length, 0)
            column = "*" * count
            print(f"{length:2} | {column:20} | {count:2}")
    else:
        print("Invalid input. Please enter an integer between 1 and {}. Terminating the program.".format(len(TEXTS)))
        quit()
# Main program
if __name__ == "__main__":
    username = login()
    print("Welcome, {}! You have access to {} texts for analysis.".format(username, len(TEXTS)))
    selected_text = input("Enter a number between 1 and {} to select: ".format(len(TEXTS)))
    analyze_text(selected_text)
    frequency(selected_text)