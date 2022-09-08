"""EX02 - One Shot Wordle."""

__author__ = "730555076"

secret_word: str = "python"
guess_word: str = input(f"What is your {len(secret_word)}-letter guess? ")

#If the guess is not the correct amount of characters
while len(guess_word) != len(secret_word):
    input(f"That was not {len(secret_word)} letters! Try again: ")

#Defining index and resulting emojis variables
index_of_word: int = 0
emojis_of_guess: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while index_of_word < len(secret_word):#producing green boxes
    if guess_word[index_of_word] == secret_word[index_of_word]:
        emojis_of_guess += GREEN_BOX
    else:#producing white and yellow boxes
        guessed_character: bool = False
        alternative_indices: int = 0
        while guessed_character is not True and alternative_indices < len(secret_word):
            if secret_word[alternative_indices] == guess_word[index_of_word]:
                guessed_character = True
            else:
                alternative_indices += 1
        if guessed_character is True:
            emojis_of_guess += YELLOW_BOX
        else:
            emojis_of_guess += WHITE_BOX
    index_of_word += 1
print(emojis_of_guess)

#If correct word is guessed
if len(guess_word) == len(secret_word):
    if str(guess_word) == str(secret_word):
        print("Woo! You got it!")
    else:#if incorrect word is guessed
        print("Not quite. Play again soon!")