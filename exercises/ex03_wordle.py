"""EX03 - Wordle."""

__author__ = "730555076"

def contains_char(wordle: str, character: str) -> bool:
    """Finding a matching character in the guessed word."""
    assert len(character) == 1
    contains_char: bool = False
    i: int = 0
    while i < len(wordle):
        if wordle[i] == character:
            return True
        else:
            i += 1
    return False

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def emojified(guess: str, secret: str) -> str:
    """Printing the string of colored box emojis."""
    assert len(guess) == len(secret)
    result: str = ""
    idx: int = 0 
    while idx < len(secret):
        if guess[idx] == secret[idx]:
            result += GREEN_BOX
        elif contains_char(secret, guess[idx]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        idx += 1
    return result

def input_guess(expected_length: int) -> int:
    guess = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess
