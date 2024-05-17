from word_guessing_game_functions import select_secret_word, initialize_game_state, play_turn, check_game_over, word_bank 

def main():
    print("Welcome to the Word Guessing Game!")
    num_players = int(input("Enter the number of players: "))
    players = [input(f"Enter the name of player {i+1}: ") for i in range(num_players)]
    
    secret_word = select_secret_word(word_bank)
    game_state = initialize_game_state(secret_word)
    
    game_over = False
    winner = None
    
    while not game_over:
        for player in players:
            if play_turn(game_state, player):
                winner = player
                game_over = True
                break
            game_over, message = check_game_over(game_state)
            if game_over:
                print(message)
                break
    
    if winner:
        print(f"\nCongratulations {winner}! You guessed the word '{secret_word}' in {game_state['turns_taken']} turns.")
    else:
        print(f"\nNo one guessed the word. The secret word was '{secret_word}'.")

if __name__ == "__main__":
    main()

