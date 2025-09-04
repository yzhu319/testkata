"""
Console UI for the Hangman game.
"""

import random
from hangman import Hangman, GuessResult, GameState


class HangmanUI:
    """Console-based user interface for the Hangman game"""
    
    def __init__(self):
        """Initialize the UI"""
        self.game = None
        self.word_list = [
            "PYTHON", "JAVA", "JAVASCRIPT", "PROGRAMMING", "COMPUTER",
            "ALGORITHM", "FUNCTION", "VARIABLE", "LOOP", "CONDITION",
            "STRING", "INTEGER", "BOOLEAN", "ARRAY", "OBJECT",
            "CLASS", "METHOD", "INHERITANCE", "POLYMORPHISM", "ENCAPSULATION"
        ]
    
    def start_game(self):
        """Start a new game"""
        print("Welcome to Hangman!")
        print("=" * 50)
        
        # Get game parameters
        word = self._get_secret_word()
        max_guesses = self._get_max_guesses()
        
        # Initialize game
        self.game = Hangman(word, max_guesses)
        
        print(f"\nGame started! The word has {len(word)} letters.")
        print(f"You have {max_guesses} incorrect guesses allowed.")
        print("Good luck!\n")
        
        # Main game loop
        self._play_game()
    
    def _get_secret_word(self) -> str:
        """Get the secret word from user or use random word"""
        print("Choose an option:")
        print("1. Enter your own word")
        print("2. Use a random word")
        
        while True:
            choice = input("Enter your choice (1 or 2): ").strip()
            if choice == "1":
                word = input("Enter the secret word: ").strip().upper()
                if word and word.replace(" ", "").isalpha():
                    return word.replace(" ", "")
                else:
                    print("Please enter a valid word (letters only).")
            elif choice == "2":
                return random.choice(self.word_list)
            else:
                print("Please enter 1 or 2.")
    
    def _get_max_guesses(self) -> int:
        """Get the maximum number of incorrect guesses"""
        while True:
            try:
                max_guesses = int(input("Enter maximum incorrect guesses (default 6): ") or "6")
                if max_guesses > 0:
                    return max_guesses
                else:
                    print("Please enter a positive number.")
            except ValueError:
                print("Please enter a valid number.")
    
    def _play_game(self):
        """Main game loop"""
        while self.game.is_in_progress:
            self._display_game_state()
            guess = self._get_guess()
            result = self.game.guess(guess)
            self._handle_guess_result(result, guess)
        
        # Game ended
        self._display_final_result()
    
    def _display_game_state(self):
        """Display the current game state"""
        print("\n" + "=" * 30)
        print(f"Word: {self.game.masked_word}")
        print(f"Incorrect guesses: {', '.join(self.game.incorrect_guesses) if self.game.incorrect_guesses else 'None'}")
        print(f"Guesses remaining: {self.game.guesses_remaining}")
        print("=" * 30)
    
    def _get_guess(self) -> str:
        """Get a guess from the user"""
        while True:
            guess = input("Enter a letter: ").strip()
            if guess:
                return guess
            print("Please enter a letter.")
    
    def _handle_guess_result(self, result: GuessResult, guess: str):
        """Handle the result of a guess"""
        if result == GuessResult.CORRECT:
            print(f"✓ Correct! '{guess.upper()}' is in the word.")
        elif result == GuessResult.INCORRECT:
            print(f"✗ Incorrect! '{guess.upper()}' is not in the word.")
        elif result == GuessResult.DUPLICATE:
            print(f"⚠ You already guessed '{guess.upper()}'.")
        elif result == GuessResult.INVALID:
            print(f"⚠ Invalid guess: '{guess}'. Please enter a single letter.")
    
    def _display_final_result(self):
        """Display the final game result"""
        print("\n" + "=" * 50)
        print(f"Final word: {self.game.masked_word}")
        print(f"Secret word was: {self.game.secret_word}")
        
        if self.game.game_state == GameState.WON:
            print("🎉 Congratulations! You won!")
        elif self.game.game_state == GameState.LOST:
            print("💀 Game over! You lost!")
        
        print("=" * 50)
    
    def play_again(self) -> bool:
        """Ask if the user wants to play again"""
        while True:
            choice = input("\nWould you like to play again? (y/n): ").strip().lower()
            if choice in ['y', 'yes']:
                return True
            elif choice in ['n', 'no']:
                return False
            else:
                print("Please enter 'y' or 'n'.")


def main():
    """Main function to run the Hangman game"""
    ui = HangmanUI()
    
    while True:
        ui.start_game()
        if not ui.play_again():
            break
    
    print("\nThanks for playing Hangman! Goodbye!")


if __name__ == "__main__":
    main()
