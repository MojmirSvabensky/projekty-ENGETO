"""
projekt_2.py: second project Engeto Online Python Academy

author: Mojmír Švábenský
email: Mojmir1@seznam.cz
discord: _bluecuracao
"""

import random
import time
import os

# Define the file path for storing the ranking data
RANKING_FILE = "ranking.txt"

# Constants for menu options
OPTION_PLAY_GAME = '1'
OPTION_SHOW_RANKING = '2'
OPTION_QUIT = '3'

# Load existing ranking data from the file, if available
player_rankings = {}
if os.path.exists(RANKING_FILE):
    with open(RANKING_FILE, "r") as file:
        for line in file:
            player, score = line.strip().split(":")
            player_rankings[player] = int(score)

def separator():
    return "-" * 48

def generate_secret_number():
    secret = random.sample(range(1, 10), 4)
    return ''.join(map(str, secret))

def get_name():
    print(separator())
    name = input("Enter your name: ")
    return name

def get_guess():
    print(separator())
    while True:
        guess = input("Enter your 4-digit guess: ")
        if len(guess) != 4 or not guess.isdigit() or len(set(guess)) < 4 or guess[0] == '0':
            print("Please enter a valid 4-digit number with unique digits and not starting with 0.")
        else:
            return guess

def count_bulls_and_cows(secret, guess):
    bulls = sum(1 for s, g in zip(secret, guess) if s == g)
    cows = sum(1 for s in secret if s in guess) - bulls
    return bulls, cows

def pluralize(n, singular, plural):
    if n == 1:
        return f"{n} {singular}"
    return f"{n} {plural}"

def get_grading(attempts):
    if attempts <= 1:
        return "Perfect"
    elif attempts <= 5:
        return "Excellent"
    elif attempts <= 12:
        return "Very Good"
    elif attempts <= 25:
        return "Good"
    elif attempts <= 35:
        return "Not So Good"
    else:
        return "Needs Improvement"

def show_best_score():
    if player_rankings:
        print("Player Rankings:")
        for rank, (player, score) in enumerate(sorted(player_rankings.items(), key=lambda x: x[1])):
            print(f"{rank + 1}. {player}: {score} attempts")
    else:
        print("No ranking data available.")

def play_game():
    print("Welcome to the Cows and Bulls game!")
    
    while True:
        print("Select an option:")
        print("1. Play the game")
        print("2. Show best score/ranking")
        print("3. Quit")
                
        option = input("Enter the option (1/2/3): ")
        print(separator())
                
        if option == OPTION_PLAY_GAME:
            instructions = """Before we start, here's how to play the Cows and Bulls game:
- The secret number is a 4-digit number with unique digits and doesn't start with 0.
- For each guess, the computer responds with the number of matching digits.
- If a digit is in its correct position, it's called a 'bull.'
- If a digit is correct, but it is in a different position, it's called a 'cow.'
- The game continues until the player guesses the secret number correctly.
"""
            print(instructions)

            player_name = get_name()
            secret_number = generate_secret_number()
            attempts = 0
            start_time = time.time()  # Record the start time

            while True:
                guess = get_guess()
                attempts += 1
                bulls, cows = count_bulls_and_cows(secret_number, guess)

                if bulls == 4:
                    end_time = time.time()  # Record the end time
                    elapsed_time = end_time - start_time  # Calculate elapsed time
                    grading = get_grading(attempts)
                    print(f"Congratulations, {player_name}! You guessed the secret number {secret_number} in {attempts} attempts.")
                    print(f"Elapsed time: {elapsed_time:.2f} seconds")
                    print(f"Your grade: {grading}")
                    # Update the player's ranking based on attempts
                    player_rankings[player_name] = attempts
                    # Save the updated ranking data to the file
                    with open(RANKING_FILE, "w") as file:
                        for player, score in player_rankings.items():
                            file.write(f"{player}:{score}\n")
                    show_best_score()
                    break
                else:
                    cows_text = pluralize(cows, "cow", "cows")
                    bulls_text = pluralize(bulls, "bull", "bulls")
                    print(f"{bulls_text}, {cows_text}")

        elif option == OPTION_SHOW_RANKING:
            show_best_score()

        elif option == OPTION_QUIT:
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please select a valid option (1/2/3).")

if __name__ == "__main__":
    play_game()
