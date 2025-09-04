"""
Test cases for the Hangman game implementation.
"""

import unittest
from hangman import Hangman, GuessResult, GameState


class TestHangman(unittest.TestCase):
    """Test cases for the Hangman class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.game = Hangman("PYTHON", 6)
    
    def test_initialization(self):
        """Test game initialization"""
        self.assertEqual(self.game.secret_word, "PYTHON")
        self.assertEqual(self.game.max_incorrect_guesses, 6)
        self.assertEqual(self.game.game_state, GameState.IN_PROGRESS)
        self.assertTrue(self.game.is_in_progress)
        self.assertEqual(self.game.guesses_remaining, 6)
        self.assertEqual(self.game.masked_word, "_ _ _ _ _ _")
        self.assertEqual(self.game.correct_guesses, [])
        self.assertEqual(self.game.incorrect_guesses, [])
    
    def test_initialization_with_custom_max_guesses(self):
        """Test initialization with custom max incorrect guesses"""
        game = Hangman("TEST", 3)
        self.assertEqual(game.max_incorrect_guesses, 3)
        self.assertEqual(game.guesses_remaining, 3)
    
    def test_initialization_case_insensitive(self):
        """Test that secret word is converted to uppercase"""
        game = Hangman("python")
        self.assertEqual(game.secret_word, "PYTHON")
    
    def test_correct_guess(self):
        """Test making a correct guess"""
        result = self.game.guess("P")
        self.assertEqual(result, GuessResult.CORRECT)
        self.assertEqual(self.game.masked_word, "P _ _ _ _ _")
        self.assertEqual(self.game.correct_guesses, ["P"])
        self.assertEqual(self.game.incorrect_guesses, [])
        self.assertEqual(self.game.guesses_remaining, 6)
        self.assertEqual(self.game.game_state, GameState.IN_PROGRESS)
    
    def test_incorrect_guess(self):
        """Test making an incorrect guess"""
        result = self.game.guess("Z")
        self.assertEqual(result, GuessResult.INCORRECT)
        self.assertEqual(self.game.masked_word, "_ _ _ _ _ _")
        self.assertEqual(self.game.correct_guesses, [])
        self.assertEqual(self.game.incorrect_guesses, ["Z"])
        self.assertEqual(self.game.guesses_remaining, 5)
        self.assertEqual(self.game.game_state, GameState.IN_PROGRESS)
    
    def test_duplicate_guess(self):
        """Test making a duplicate guess"""
        self.game.guess("P")
        result = self.game.guess("P")
        self.assertEqual(result, GuessResult.DUPLICATE)
        self.assertEqual(self.game.correct_guesses, ["P"])
        self.assertEqual(self.game.incorrect_guesses, [])
    
    def test_duplicate_incorrect_guess(self):
        """Test making a duplicate incorrect guess"""
        self.game.guess("Z")
        result = self.game.guess("Z")
        self.assertEqual(result, GuessResult.DUPLICATE)
        self.assertEqual(self.game.incorrect_guesses, ["Z"])
    
    def test_invalid_guess_empty_string(self):
        """Test making an invalid guess with empty string"""
        result = self.game.guess("")
        self.assertEqual(result, GuessResult.INVALID)
    
    def test_invalid_guess_multiple_characters(self):
        """Test making an invalid guess with multiple characters"""
        result = self.game.guess("AB")
        self.assertEqual(result, GuessResult.INVALID)
    
    def test_invalid_guess_non_alpha(self):
        """Test making an invalid guess with non-alphabetic character"""
        result = self.game.guess("1")
        self.assertEqual(result, GuessResult.INVALID)
        result = self.game.guess("@")
        self.assertEqual(result, GuessResult.INVALID)
    
    def test_guess_case_insensitive(self):
        """Test that guesses are case insensitive"""
        result = self.game.guess("p")
        self.assertEqual(result, GuessResult.CORRECT)
        self.assertEqual(self.game.correct_guesses, ["P"])
    
    def test_guess_with_whitespace(self):
        """Test that guesses with whitespace are handled correctly"""
        result = self.game.guess(" P ")
        self.assertEqual(result, GuessResult.CORRECT)
        self.assertEqual(self.game.correct_guesses, ["P"])
    
    def test_multiple_correct_guesses(self):
        """Test making multiple correct guesses"""
        self.game.guess("P")
        self.game.guess("Y")
        self.game.guess("T")
        
        self.assertEqual(self.game.masked_word, "P Y T _ _ _")
        self.assertEqual(self.game.correct_guesses, ["P", "T", "Y"])
        self.assertEqual(self.game.incorrect_guesses, [])
        self.assertEqual(self.game.guesses_remaining, 6)
    
    def test_multiple_incorrect_guesses(self):
        """Test making multiple incorrect guesses"""
        self.game.guess("A")
        self.game.guess("B")
        self.game.guess("C")
        
        self.assertEqual(self.game.masked_word, "_ _ _ _ _ _")
        self.assertEqual(self.game.correct_guesses, [])
        self.assertEqual(self.game.incorrect_guesses, ["A", "B", "C"])
        self.assertEqual(self.game.guesses_remaining, 3)
    
    def test_win_condition(self):
        """Test winning the game by guessing all letters"""
        # Guess all letters in PYTHON
        self.game.guess("P")
        self.game.guess("Y")
        self.game.guess("T")
        self.game.guess("H")
        self.game.guess("O")
        self.game.guess("N")
        
        self.assertEqual(self.game.game_state, GameState.WON)
        self.assertFalse(self.game.is_in_progress)
        self.assertEqual(self.game.masked_word, "P Y T H O N")
        self.assertEqual(self.game.guesses_remaining, 6)
    
    def test_lose_condition(self):
        """Test losing the game by making too many incorrect guesses"""
        # Make 6 incorrect guesses
        for letter in "ABCDEF":
            result = self.game.guess(letter)
            self.assertEqual(result, GuessResult.INCORRECT)
        
        self.assertEqual(self.game.game_state, GameState.LOST)
        self.assertFalse(self.game.is_in_progress)
        self.assertEqual(self.game.guesses_remaining, 0)
    
    def test_guessing_after_game_ended(self):
        """Test that guessing after game ends returns invalid"""
        # Win the game
        for letter in "PYTHON":
            self.game.guess(letter)
        
        # Try to guess after winning
        result = self.game.guess("X")
        self.assertEqual(result, GuessResult.INVALID)
    
    def test_guessing_after_losing(self):
        """Test that guessing after losing returns invalid"""
        # Lose the game
        for letter in "ABCDEF":
            self.game.guess(letter)
        
        # Try to guess after losing
        result = self.game.guess("X")
        self.assertEqual(result, GuessResult.INVALID)
    
    def test_word_with_repeated_letters(self):
        """Test guessing a word with repeated letters"""
        game = Hangman("HELLO", 6)
        result = game.guess("L")
        self.assertEqual(result, GuessResult.CORRECT)
        self.assertEqual(game.masked_word, "_ _ L L _")
        self.assertEqual(game.correct_guesses, ["L"])
    
    def test_string_representation(self):
        """Test string representation of the game"""
        self.game.guess("P")
        self.game.guess("Z")
        
        expected = "Word: P _ _ _ _ _ | Incorrect: Z | Remaining: 5 | State: in_progress"
        self.assertEqual(str(self.game), expected)
    
    def test_repr_representation(self):
        """Test detailed string representation"""
        repr_str = repr(self.game)
        self.assertIn("Hangman", repr_str)
        self.assertIn("secret_word='PYTHON'", repr_str)
        self.assertIn("max_incorrect_guesses=6", repr_str)
        self.assertIn("state=in_progress", repr_str)


class TestHangmanEdgeCases(unittest.TestCase):
    """Test edge cases for the Hangman class"""
    
    def test_single_letter_word(self):
        """Test game with single letter word"""
        game = Hangman("A", 3)
        result = game.guess("A")
        self.assertEqual(result, GuessResult.CORRECT)
        self.assertEqual(game.game_state, GameState.WON)
        self.assertEqual(game.masked_word, "A")
    
    def test_word_with_spaces(self):
        """Test game with word containing spaces (if supported)"""
        # Note: This test assumes spaces are not valid letters
        game = Hangman("HELLO WORLD", 6)
        result = game.guess(" ")
        self.assertEqual(result, GuessResult.INVALID)
    
    def test_zero_max_incorrect_guesses(self):
        """Test game with zero max incorrect guesses"""
        game = Hangman("TEST", 0)
        result = game.guess("Z")
        self.assertEqual(result, GuessResult.INCORRECT)
        self.assertEqual(game.game_state, GameState.LOST)
    
    def test_very_long_word(self):
        """Test game with a very long word"""
        long_word = "SUPERCALIFRAGILISTICEXPIALIDOCIOUS"
        game = Hangman(long_word, 10)
        expected_masked = " ".join("_" * len(long_word))
        self.assertEqual(game.masked_word, expected_masked)
        self.assertEqual(game.secret_word, long_word)


if __name__ == '__main__':
    unittest.main()
