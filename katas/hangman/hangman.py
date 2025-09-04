"""
Hangman Game Implementation

A word guessing game where players try to guess a secret word by guessing letters.
"""

from enum import Enum
from typing import List, Set


class GuessResult(Enum):
    """Result of a guess attempt"""
    INVALID = "invalid"
    INCORRECT = "incorrect"
    CORRECT = "correct"
    DUPLICATE = "duplicate"


class GameState(Enum):
    """Current state of the game"""
    IN_PROGRESS = "in_progress"
    WON = "won"
    LOST = "lost"


class Hangman:
    """
    Hangman game implementation.
    
    The game tracks a secret word, allows players to guess letters,
    and determines win/loss conditions based on incorrect guesses.
    """
    
    def __init__(self, secret_word: str, max_incorrect_guesses: int = 6):
        """
        Initialize a new Hangman game.
        
        Args:
            secret_word: The word to be guessed (will be converted to uppercase)
            max_incorrect_guesses: Maximum number of incorrect guesses allowed
        """
        self._secret_word = secret_word.upper()
        self._max_incorrect_guesses = max_incorrect_guesses
        self._correct_guesses: Set[str] = set()
        self._incorrect_guesses: Set[str] = set()
        self._all_guesses: Set[str] = set()
        self._game_state = GameState.IN_PROGRESS
    
    @property
    def secret_word(self) -> str:
        """Get the secret word in uppercase"""
        return self._secret_word
    
    @property
    def max_incorrect_guesses(self) -> int:
        """Get the maximum number of incorrect guesses allowed"""
        return self._max_incorrect_guesses
    
    @property
    def game_state(self) -> GameState:
        """Get the current game state"""
        return self._game_state
    
    @property
    def is_in_progress(self) -> bool:
        """Check if the game is still in progress"""
        return self._game_state == GameState.IN_PROGRESS
    
    @property
    def correct_guesses(self) -> List[str]:
        """Get list of correctly guessed letters"""
        return sorted(list(self._correct_guesses))
    
    @property
    def incorrect_guesses(self) -> List[str]:
        """Get list of incorrectly guessed letters"""
        return sorted(list(self._incorrect_guesses))
    
    @property
    def guesses_remaining(self) -> int:
        """Get number of incorrect guesses remaining"""
        return self._max_incorrect_guesses - len(self._incorrect_guesses)
    
    @property
    def masked_word(self) -> str:
        """
        Get the secret word with unguessed letters masked.
        Correctly guessed letters are shown, others are shown as underscores.
        """
        result = []
        for letter in self._secret_word:
            if letter in self._correct_guesses:
                result.append(letter)
            else:
                result.append('_')
        return ' '.join(result)
    
    def guess(self, letter: str) -> GuessResult:
        """
        Make a guess for a letter.
        
        Args:
            letter: The letter to guess (case insensitive)
            
        Returns:
            GuessResult indicating the result of the guess
        """
        if self._game_state != GameState.IN_PROGRESS:
            return GuessResult.INVALID
        
        # Normalize the input
        letter = letter.upper().strip()
        
        # Validate the letter
        if not self._is_valid_letter(letter):
            return GuessResult.INVALID
        
        # Check for duplicate guess
        if letter in self._all_guesses:
            return GuessResult.DUPLICATE
        
        # Record the guess
        self._all_guesses.add(letter)
        
        # Check if letter is in the word
        if letter in self._secret_word:
            self._correct_guesses.add(letter)
            self._update_game_state()
            return GuessResult.CORRECT
        else:
            self._incorrect_guesses.add(letter)
            self._update_game_state()
            return GuessResult.INCORRECT
    
    def _is_valid_letter(self, letter: str) -> bool:
        """
        Check if a letter is valid for guessing.
        
        Args:
            letter: The letter to validate
            
        Returns:
            True if the letter is valid, False otherwise
        """
        return len(letter) == 1 and letter.isalpha()
    
    def _update_game_state(self):
        """Update the game state based on current progress"""
        # Check if all letters have been guessed
        if all(letter in self._correct_guesses for letter in self._secret_word):
            self._game_state = GameState.WON
        # Check if too many incorrect guesses
        elif len(self._incorrect_guesses) >= self._max_incorrect_guesses:
            self._game_state = GameState.LOST
        else:
            self._game_state = GameState.IN_PROGRESS
    
    def __str__(self) -> str:
        """String representation of the game state"""
        return (f"Word: {self.masked_word} | "
                f"Incorrect: {', '.join(self.incorrect_guesses)} | "
                f"Remaining: {self.guesses_remaining} | "
                f"State: {self.game_state.value}")
    
    def __repr__(self) -> str:
        """Detailed string representation for debugging"""
        return (f"Hangman(secret_word='{self._secret_word}', "
                f"max_incorrect_guesses={self._max_incorrect_guesses}, "
                f"state={self._game_state.value})")
