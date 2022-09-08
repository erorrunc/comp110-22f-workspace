"""EX02 - One Shot Wordle."""

__author__ = "730555076"

secret_word: str = "python"
guess_word: str = input(f"What is your {len(secret_word)}-letter guess? ")

# if the guess is not the correct amount of characters
while len(guess_word) != len(secret_word):
    guess_word = input(f"That was not {len(secret_word)} letters! Try again: ")

# defining index of secret word and resulting emojis variables
i: int = 0
result: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while i < len(secret_word):# producing green boxes
    if guess_word[i] == secret_word[i]:
        result += GREEN_BOX
    else:# producing white and yellow boxes
        guessed_character: bool = False
        idx: int = 0
        while guessed_character is not True and idx < len(secret_word):
            if secret_word[idx] == guess_word[i]:
                guessed_character = True
            else:
                idx += 1
        if guessed_character is True:
            result += YELLOW_BOX
        else:
            result += WHITE_BOX
    i += 1
print(result)

if len(guess_word) == len(secret_word):
    if str(guess_word) == str(secret_word):# when the correct word is guessed
        print("Woo! You got it!")
    else:# when an incorrect word is guessed
        print("Not quite. Play again soon!")