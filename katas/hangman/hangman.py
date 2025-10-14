"""
Simple Hangman Game - Interview Version
"""

class Hangman:
    def __init__(self, word, max_guesses):
        self.word = word.upper()
        self.max_guesses = max_guesses
        self.guesses = []
        self.correct_guesses = set()
        self.incorrect_guesses = set()
        self.status = "GameIsOn"
    
    def guess(self, letter):
        if self.status != "GameIsOn":
            return "GameOver"
        
        letter = letter.upper()
        
        # Invalid guess
        if len(letter) != 1 or not letter.isalpha():
            return "InvalidGuess"
        
        # Duplicate guess
        if letter in self.guesses:
            return "DuplicateGuess"
        
        self.guesses.append(letter)
        
        if letter in self.word:
            self.correct_guesses.add(letter)
            if self._is_won():
                self.status = "GameWon"
            return "CorrectGuess"
        else:
            self.incorrect_guesses.add(letter)
            if len(self.incorrect_guesses) >= self.max_guesses:
                self.status = "GameLost"
            return "IncorrectGuess"
    
    def _is_won(self):
        return all(letter in self.correct_guesses for letter in self.word)
    
    def _get_display_word(self):
        return ''.join(letter if letter in self.correct_guesses else '-' for letter in self.word)
    
    def get_display_word(self):
        """Get the word with guessed letters revealed"""
        return self._get_display_word()