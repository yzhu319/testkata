# Hangman Game Implementation

A Python implementation of the classic Hangman word guessing game, created as part of the kata-catalog collection.

## Files

- `hangman.py` - Core game logic and Hangman class
- `test_hangman.py` - Comprehensive test suite
- `hangman_ui.py` - Console-based user interface
- `README.md` - This documentation

## Features

### Core Game Logic (`hangman.py`)

The `Hangman` class provides:

- **Game Initialization**: Accepts a secret word and maximum incorrect guesses
- **Letter Guessing**: Validates and processes letter guesses
- **Game State Tracking**: Monitors win/loss conditions and progress
- **Result Types**: Returns appropriate results for different guess scenarios
- **Properties**: Access to masked word, remaining guesses, game state, etc.

### Key Methods

- `guess(letter)` - Make a letter guess and get the result
- `masked_word` - Get the word with unguessed letters hidden
- `guesses_remaining` - Get number of incorrect guesses left
- `game_state` - Get current game state (in_progress, won, lost)

### Result Types

- `CORRECT` - Letter is in the word
- `INCORRECT` - Letter is not in the word
- `DUPLICATE` - Letter was already guessed
- `INVALID` - Invalid input (non-letter, multiple characters, etc.)

## Running the Game

### Console UI

To play the game with the console interface:

```bash
python hangman_ui.py
```

The UI allows you to:
- Choose your own word or use a random word
- Set the maximum number of incorrect guesses
- Play multiple rounds
- See visual feedback for each guess

### Programmatic Usage

```python
from hangman import Hangman, GuessResult, GameState

# Create a new game
game = Hangman("PYTHON", 6)

# Make guesses
result = game.guess("P")  # Returns GuessResult.CORRECT
result = game.guess("Z")  # Returns GuessResult.INCORRECT

# Check game state
print(game.masked_word)  # "P _ _ _ _ _"
print(game.guesses_remaining)  # 5
print(game.game_state)  # GameState.IN_PROGRESS
```

## Running Tests

To run the comprehensive test suite:

```bash
python -m unittest test_hangman.py
```

Or with verbose output:

```bash
python -m unittest -v test_hangman.py
```

The test suite covers:
- Game initialization and properties
- Correct and incorrect guesses
- Duplicate and invalid guesses
- Win and loss conditions
- Edge cases and error handling
- String representations

## Game Rules

1. A secret word is chosen (converted to uppercase)
2. Player guesses letters one at a time
3. Correct letters are revealed in their positions
4. Incorrect letters are tracked and count against the limit
5. Game ends when:
   - All letters are guessed (WIN)
   - Maximum incorrect guesses reached (LOSS)

## Requirements Met

This implementation fulfills all requirements from the original kata:

✅ **Class Creation**: `Hangman` class with secret word and max incorrect guesses  
✅ **Game State**: Property indicating game is in progress  
✅ **Guess Method**: Returns appropriate results for different scenarios  
✅ **Validation**: Handles invalid characters and duplicate guesses  
✅ **State Calculation**: Tracks win/loss conditions after each guess  
✅ **UI Features**: Console interface with all required display elements  

## Design Decisions

- **Case Insensitive**: All input is normalized to uppercase
- **Single Letter Validation**: Only alphabetic characters are valid
- **Immutable Game State**: Once won/lost, no further guesses allowed
- **Comprehensive Testing**: Full test coverage including edge cases
- **Clean API**: Simple, intuitive interface for both programmatic and UI usage
