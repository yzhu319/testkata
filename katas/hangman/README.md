# Hangman Game - Interview Solution

## Whiteboard Solution & Thought Process

### Problem Understanding
**Goal**: Create a word guessing game where players guess letters of a secret word.

**Core Requirements**:
1. Track a secret word and max incorrect guesses
2. Accept letter guesses and return results
3. Handle invalid/duplicate guesses
4. Determine win/loss conditions
5. Display game state

### Whiteboard Design

```
Hangman Class
├── word: str (secret word)
├── max_guesses: int (max wrong guesses)
├── guesses: list (all guesses made)
├── correct_guesses: set (letters in word)
├── incorrect_guesses: set (letters not in word)
└── status: str (GameIsOn/GameWon/GameLost)

Methods:
├── __init__(word, max_guesses)
├── guess(letter) -> result
└── __str__() -> game state
```

### Thought Process

**1. Data Structure Choice**
- `guesses: list` - Keep order of guesses for display
- `correct_guesses: set` - Fast lookup for win condition
- `incorrect_guesses: set` - Fast lookup for loss condition

**2. Guess Logic Flow**
```
Input letter
├── Game over? → Exception
├── Invalid? → "InvalidGuess"
├── Duplicate? → "DuplicateGuess"
├── In word? → "CorrectGuess" + check win
└── Not in word? → "IncorrectGuess" + check loss
```

**3. Win/Loss Conditions**
- **Win**: All letters in word have been guessed
- **Loss**: Number of incorrect guesses >= max_guesses

**4. Status-Based Design**
- No exceptions - returns `"GameOver"` when game ends
- UI handles game flow and prevents guessing after game over
- Simple, predictable behavior for testing

### Key Design Decisions

**Why this approach?**
1. **Simple State Management**: Single status field instead of complex state machine
2. **Efficient Lookups**: Sets for O(1) letter checking
3. **Clear Return Values**: String constants for easy testing
4. **Minimal Code**: Focus on core functionality, avoid over-engineering

**Trade-offs Made**:
- ✅ Simple to understand and implement
- ✅ Easy to test with string comparisons
- ✅ Minimal dependencies
- ❌ Less extensible (but that's OK for interview)
- ❌ No fancy design patterns (intentionally)

### Implementation Strategy

**Phase 1: Core Logic**
1. Create Hangman class with basic fields
2. Implement guess() method with validation
3. Add win/loss detection
4. Create string representation

**Phase 2: Testing**
1. Copy approval test scenarios
2. Verify exact string outputs match
3. Test edge cases (invalid input, game over)

**Phase 3: UI (if time permits)**
1. Simple console input/output
2. Basic game loop
3. Display game state

### Interview Tips

**What to explain first:**
1. "I'll start with the core Hangman class"
2. "The key challenge is tracking game state efficiently"
3. "I'll use sets for fast letter lookups"

**What to focus on:**
1. Clean, readable code
2. Proper input validation
3. Clear win/loss logic
4. Easy-to-test string output

**Common pitfalls to avoid:**
1. Over-engineering with complex state machines
2. Not handling edge cases (invalid input, game over)
3. Making the code too verbose for interview time

## Files

- `hangman.py` - Core game logic (35 lines)
- `test_hangman.py` - Test cases based on approval tests
- `hangman_ui.py` - Simple console interface
- `README.md` - This documentation

## Usage

**Run tests:**
```bash
python -m unittest test_hangman.py
```

**Play game:**
```bash
python hangman_ui.py
```

**Use programmatically:**
```python
game = Hangman("BELL", 3)
result = game.guess("L")  # "CorrectGuess"
print(game.status)  # "GameIsOn"
print(game.get_display_word())  # "--LL"
print(game.guesses)  # ["L"]

# After game ends
result = game.guess("X")  # "GameOver"
print(game.status)  # "GameWon" or "GameLost"
```

## Next Steps (If Time Permits)

1. **Add duplicate guess handling** (currently returns "DuplicateGuess")
2. **Improve UI** with better formatting
3. **Add word list** for random word selection
4. **Add difficulty levels** with different max guesses
5. **Add ASCII art** for hangman drawing