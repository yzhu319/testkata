"""
Simple test cases for Hangman - Interview Version
"""

import unittest
from hangman import Hangman

class TestHangman(unittest.TestCase):
    
    def test_basic_functionality(self):
        """Test basic game functionality"""
        game = Hangman("BELL", 3)
        
        # Initial state
        self.assertEqual("GameIsOn", game.status)
        self.assertEqual("----", game.get_display_word())
        self.assertEqual([], game.guesses)
        self.assertEqual(3, game.max_guesses)
        
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

if __name__ == '__main__':
    unittest.main()