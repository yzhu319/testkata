"""
Hangman Game - Ultra Simple Version
Perfect for CoderPad interviews - minimal code
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


def simulation():
    hangman = Hangman(input("Input word: ").strip().upper(), 6)
    while hangman.status == 'GameIsOn':
        input_letter = input("Input a letter: ").upper()
        result = hangman.guess(input_letter)

        if result == 'InvalidGuess':
            print('invalid guess')
        elif result == 'DuplicateGuess':
            print('DuplicateGuess')
        elif result == 'CorrectGuess':
            print('CorrectGuess')
        elif result == 'IncorrectGuess':
            print('IncorrectGuess')
        
        print(hangman.display_status())

    if hangman.status == 'GameWon':
        print('Game is Won')
    elif hangman.status == 'GameLost':
        print('Game is Lost')


import unittest

class TestHangman(unittest.TestCase):
    def test_win(self):
        hangman = Hangman('APPLE', 6)
        hangman.guess('a')
        hangman.guess('p')
        hangman.guess('l')
        hangman.guess('e')
        self.assertEqual(hangman.status, 'GameWon')

    def test_lost(self):
        hangman = Hangman('APPLE', 6)
        hangman.guess('b')
        hangman.guess('c')
        hangman.guess('d')
        hangman.guess('k')
        hangman.guess('q')
        hangman.guess('r')
        self.assertEqual(hangman.status, 'GameLost')

unittest.main()
