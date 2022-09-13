"""EX03 - Wordle."""

__author__ = "730555076"


def contains_char(word: str, character: str) -> bool:
    """Finding a matching character in the guess word."""
    assert len(character) == 1
    contains_char: bool = False
    i: int = 0
    while i < len(word):  # determining if a letter is contained in a word
        if word[i] == character:
            return True
        else:
            i += 1
    return False


# assigning emoji variables
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Printing the colored box emojis of the guess word compared to the secret word."""
    assert len(guess) == len(secret)
    result: str = ""
    i: int = 0
    while i < len(secret):  # determining which colored boxes to print based on how the guessed word matches up to the secret word
        if guess[i] == secret[i]:
            result += GREEN_BOX
        elif contains_char(secret, guess[i]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
        i += 1
    return result


def input_guess(expected_length: int) -> str:
    """Prompt user for a guess until their guess matches the expected length."""
    guess: str = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:  # making sure the user's guess is the correct length
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main() -> None:
    """The entry point of the program and main game loop."""
    N: int = 1
    secret: str = "codes"
    guess: str = ""
    result: str = ""
    while N <= 6 and guess != secret:  # loop while the user is guessing and the guess is not correct
        print(f"=== Turn {N}/6 ===")
        guess = input_guess(5)
        result = emojified(guess, secret)
        print(result)
        N = N + 1
    if guess == secret:  # end result of the wordle
        print(f"You won in {N-1}/6 turns!") 
    if guess != secret:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()