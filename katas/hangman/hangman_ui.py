"""
Simple Hangman Console UI - Interview Version
"""

from hangman import Hangman

def play_hangman():
    """Simple console game"""
    print("=== HANGMAN GAME ===")
    
    # Get word from user
    word = input("Enter a word: ").strip().upper()
    if not word:
        word = "PYTHON"  # Default word
    
    # Create game
    game = Hangman(word, 6)
    
    print(f"\nWord: {game.get_display_word()}")
    print(f"Guesses left: {game.max_guesses}")
    
    # Game loop
    while game.status == "GameIsOn":
        guess = input("\nGuess a letter: ").strip()
        
        if not guess:
            continue
            
        result = game.guess(guess)
        
        if result == "CorrectGuess":
            print("✓ Correct!")
        elif result == "IncorrectGuess":
            print("✗ Wrong!")
        elif result == "InvalidGuess":
            print("⚠ Invalid guess!")
        elif result == "DuplicateGuess":
            print("⚠ Already guessed!")
        elif result == "GameOver":
            print("⚠ Game is already over!")
            break
        
        print(f"Word: {game.get_display_word()}")
        print(f"Guesses: {' '.join(game.guesses)}")
        print(f"Guesses left: {game.max_guesses - len(game.incorrect_guesses)}")
    
    # Game over
    if game.status == "GameWon":
        print("\n🎉 You won!")
    else:
        print("\n💀 You lost!")
    
    print(f"The word was: {game.word}")

if __name__ == "__main__":
    play_hangman()