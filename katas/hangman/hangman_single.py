"""
Hangman Game - Single File Implementation
Perfect for CoderPad interviews
"""

class Hangman:
    def __init__(self, word, maxGuesses):
        self.word = word.upper()
        self.maxGuesses = maxGuesses
        self.correctGuess = set()  # decide win/lose
        self.incorrectGuess = set()  # decide lose 
        self.guesses = []
        self.status = 'GameIsOn'  # 3 status: 'GameIsOn', 'GameWon', 'GameLost'

    def _is_won(self):
        return all(l in self.correctGuess for l in self.word)
    
    def guess(self, letter):
        # Check if game is over
        if self.status != 'GameIsOn':
            return 'GameOver'
            
        letter = letter.upper()

        if len(letter) != 1 or not letter.isalpha():
            return 'InvalidGuess'
        
        if letter in self.guesses:
            return 'DuplicateGuess'

        self.guesses.append(letter)

        if letter in self.word:
            self.correctGuess.add(letter)
            if self._is_won():
                self.status = 'GameWon'
            return 'CorrectGuess'

        else:
            self.incorrectGuess.add(letter)
            if len(self.incorrectGuess) >= self.maxGuesses:
                self.status = 'GameLost'
            return 'IncorrectGuess'

    def display_status(self):
        display_msg = ''.join(l if l in self.correctGuess else '-' for l in self.word)
        return display_msg + '; remain ' + str(self.maxGuesses - len(self.incorrectGuess))

    def get_display_word(self):
        """Get the word with guessed letters revealed"""
        return ''.join(l if l in self.correctGuess else '-' for l in self.word)


# UI Simulation
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
    print(f"Guesses left: {game.maxGuesses}")
    
    # Game loop with explicit status check
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
        print(f"Guesses left: {game.maxGuesses - len(game.incorrectGuess)}")
        
        # Additional check after each guess to enforce game ending
        if game.status != "GameIsOn":
            break
    
    # Game over handling
    if game.status == "GameWon":
        print("\n🎉 You won!")
    elif game.status == "GameLost":
        print("\n💀 You lost!")
    
    print(f"The word was: {game.word}")


# Test Suite
import unittest

class TestHangman(unittest.TestCase):
    
    def test_basic_functionality(self):
        """Test basic game functionality"""
        game = Hangman("BELL", 3)
        
        # Initial state
        self.assertEqual("GameIsOn", game.status)
        self.assertEqual("----", game.get_display_word())
        self.assertEqual([], game.guesses)
        self.assertEqual(3, game.maxGuesses)
        
        # Correct guess
        result = game.guess("L")
        self.assertEqual("CorrectGuess", result)
        self.assertEqual("GameIsOn", game.status)
        self.assertEqual("--LL", game.get_display_word())
        self.assertEqual(["L"], game.guesses)
        
        # Incorrect guess
        result = game.guess("X")
        self.assertEqual("IncorrectGuess", result)
        self.assertEqual("GameIsOn", game.status)
        self.assertEqual("--LL", game.get_display_word())
        self.assertEqual(["L", "X"], game.guesses)
        
        # Invalid guess (should not change state)
        result = game.guess("#")
        self.assertEqual("InvalidGuess", result)
        self.assertEqual("GameIsOn", game.status)
        self.assertEqual("--LL", game.get_display_word())
        self.assertEqual(["L", "X"], game.guesses)
        
        # Duplicate guess
        result = game.guess("L")
        self.assertEqual("DuplicateGuess", result)
        self.assertEqual("GameIsOn", game.status)
        self.assertEqual("--LL", game.get_display_word())
        self.assertEqual(["L", "X"], game.guesses)
    
    def test_win_condition(self):
        """Test winning the game"""
        game = Hangman("BELL", 3)
        
        # Guess all letters
        game.guess("B")
        game.guess("E")
        game.guess("L")
        
        self.assertEqual("GameWon", game.status)
        self.assertEqual("BELL", game.get_display_word())
        
        # Can't guess after winning
        result = game.guess("X")
        self.assertEqual("GameOver", result)
    
    def test_lose_condition(self):
        """Test losing the game"""
        game = Hangman("BELL", 2)
        
        # Make 2 incorrect guesses
        game.guess("X")
        game.guess("Y")
        
        self.assertEqual("GameLost", game.status)
        self.assertEqual("----", game.get_display_word())
        
        # Can't guess after losing
        result = game.guess("B")
        self.assertEqual("GameOver", result)
    
    def test_edge_cases(self):
        """Test edge cases"""
        # Single letter word
        game = Hangman("A", 1)
        game.guess("A")
        self.assertEqual("GameWon", game.status)
        
        # Zero max guesses
        game = Hangman("TEST", 0)
        result = game.guess("X")
        self.assertEqual("IncorrectGuess", result)
        self.assertEqual("GameLost", game.status)


# Your original ad-hoc test (commented out)
"""
hangman = Hangman('apple', 2)
print(hangman.display_status())
print(hangman.guess('a'))
print(hangman.display_status())
print(hangman.guess('p'))
print(hangman.display_status())
print(hangman.guess('t'))
print(hangman.display_status())
print(hangman.guess('p'))
print(hangman.display_status())
print(hangman.guess('z'))
print(hangman.display_status())
print(hangman.guess('q'))
print(hangman.display_status())
"""


if __name__ == "__main__":
    # Run tests
    print("Running tests...")
    unittest.main(verbosity=2, exit=False)
    
    # Uncomment to play the game
    # play_hangman()
