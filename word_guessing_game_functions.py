import random

# Sample bank of words
word_bank = ['carrot', 'rotation', 'cat', 'sandwich', 'fish', 'bloody']

def select_secret_word(word_bank):
    """Randomly selects a word from the word bank and labels it as secret."""
    return random.choice(word_bank)

def initialize_game_state(secret_word):
    """Initializes the game state for a new game."""
    return {
        'secret_word': secret_word,
        'letter_guesses': set(),
        'word_guesses': 0,
        'turns_taken': 0,
        'max_word_guesses': 3
    }

def display_letter_guesses(game_state):
    """Displays the letters guessed so far."""
    letter_guesses = game_state['letter_guesses']
    print(f"Letter guesses: {', '.join(sorted(letter_guesses))}")
    print(f"Word guesses remaining: {game_state['max_word_guesses'] - game_state['word_guesses']}")

def process_letter_guess(game_state, letter):
    """Processes a letter guess."""
    secret_word = game_state['secret_word']
    game_state['letter_guesses'].add(letter)
    game_state['turns_taken'] += 1
    return secret_word.count(letter)

def process_word_guess(game_state, guess):
    """Processes a word guess."""
    game_state['word_guesses'] += 1
    return game_state['secret_word'] == guess

def check_game_over(game_state):
    """Checks if the game is over."""
    if game_state['word_guesses'] >= game_state['max_word_guesses']:
        return True, "You've used all your word guesses! Game Over."
    
    secret_word = game_state['secret_word']
    letter_guesses = game_state['letter_guesses']
    if all(letter in letter_guesses for letter in secret_word):
        return True, f"Congratulations! You've guessed the word '{secret_word}' in {game_state['turns_taken']} turns."
    
    return False, ""

def play_turn(game_state, player_name):
    """Plays a single turn for a player."""
    print(f"\n{player_name}'s turn!")
    display_game_state(game_state)
    
    letter = input("Guess a letter: ").lower()
    occurrences = process_letter_guess(game_state, letter)
    print(f"The letter '{letter}' occurs {occurrences} time(s) in the word.")
    
    guess_word = input("Do you want to guess the word? (yes/no): ").lower()
    if guess_word == 'yes':
        word_guess = input("Enter your word guess: ").lower()
        if process_word_guess(game_state, word_guess):
            return True
        else:
            print(f"'{word_guess}' is not the secret word.")
    
    return False
