"""EX06 - Choose your own adventure: Harry Potter Sorting Quiz."""

__author__ = "730555076"


# Emoji variables and global variables
MAGIC_WAND_EMOJI: str = "\U0001FA84 "
PARCHMENT_EMOJI: str = "\U0001F4DC "
BOLT_EMOJI: str = "\U000026A1 "
points: int
player: str


# "Adventure points" track a person's score throughout the quiz
# Depending on a person's score, they are sorted to a particular house
def main() -> None:
    """Initializes adventure points and gives player a choice to begin."""
    global points
    points = 0
    greet()
    choice: str = input("Type '1' to start a new quiz, '2' to change player name, and '3' to exit the quiz. \nType here: ")

# Game Loop
    continue_game: bool = True
    while continue_game is True:
        if choice == "3":
            print(f"Thanks for playing! Your total score is {points} adventure points, and you were not able to be sorted into a house.")
            continue_game = False
            return
            
        elif choice == "1":
            points = 0
            question_1()
            question_2()
            question_3()
            points = question_4(points)
            question_5()
            fate()

            house: str = resulting_house()
            end_game: str = (f"\nYou were sorted into: {house}! {MAGIC_WAND_EMOJI} {PARCHMENT_EMOJI} Thank you for playing! Your total score is {points} adventure points. \n")
            print(end_game)
            choice = input(f"Your total score is {points} points. To play again and start your points over, type '1', to change player name and play again, type '2', and to exit the game, type '3'. \nType here: ")
            if choice == "3":
                continue_game = False
            
        elif choice == "2":
            change_name()
            points = 0
            question_1()
            question_2()
            question_3()
            points = question_4(points)
            question_5()
            fate()

            house = resulting_house()
            end_game = (f"\nYou were sorted into: {house}! {MAGIC_WAND_EMOJI} {PARCHMENT_EMOJI}Thank you for playing! Your total score is {points} adventure points. \n")
            print(end_game)
            choice = input(f"Your total score is {points} points. To play again and start your points over, type '1', to change player name and play again, type '2', and to exit the game, type '3'. \nType here: ")
            if choice == "3":
                continue_game = False

        else:
            choice = input("That wasn't an option! Try again: ")


# Welcoming players, introduction to the quiz
def greet() -> None:
    """Welcomes the player and asks for player name."""
    global player

    print(f"Welcome, young wizards and witches! {MAGIC_WAND_EMOJI} {PARCHMENT_EMOJI} Take this short quiz to find out what Hogwarts house you will be sorted into.")
    player = input("What is your name? ")


# Option 2, changing player name
def change_name() -> None:
    """If player selects option 2, allows player to change their name."""
    global player
    player = input("What would you like to change your name to? ")


# Question 1
def question_1() -> None:
    """Question 1 of quiz."""
    global points
    global player

    input(f"Hello, {player}! For each question, type the letter choice that best applies to you. Ready? Press Enter to continue.")
    print(f"\n{BOLT_EMOJI} Question 1 {BOLT_EMOJI} \n{player}, what is your favorite time of day? \nA: Bright and early in the morning. \nB: Lunch time and early afternoon. \nC: Evening and sunset. \nD: The few hours before midnight.")

    answer: str = input("Answer: ")
    valid_answer: bool = False
    while valid_answer is False:
        # Ravenclaw
        if answer == "A":
            points += 2
            valid_answer = True
        # Hufflepuff
        elif answer == "B":
            points += 1
            valid_answer = True
        # Gryffindor
        elif answer == "C":
            points += 3
            valid_answer = True
        # Slytherin
        elif answer == "D":
            points += 4
            valid_answer = True
        else:
            answer = input("That wasn't an answer choice! Try again: ")


# Question 2
def question_2() -> None:
    """Question 2 of quiz."""
    global points
    
    print(f"\n{BOLT_EMOJI} Question 2 {BOLT_EMOJI} \nWhat element do you feel most represents you? \nA: Water. \nB: Fire. \nC: Air. \nD: Earth.")

    answer: str = input("Answer: ")
    valid_answer: bool = False
    while valid_answer is False:
        # Ravenclaw
        if answer == "A":
            points += 2
            valid_answer = True
        # Gryffindor
        elif answer == "B":
            points += 3
            valid_answer = True
        # Hufflepuff
        elif answer == "C":
            points += 1
            valid_answer = True
        # Slytherin
        elif answer == "D":
            points += 4
            valid_answer = True
        else:
            answer = input("That wasn't an answer choice! Try again: ")


# Question 3
def question_3() -> None:
    """Question 3 of quiz."""
    global points
    global player

    print(f"\n{BOLT_EMOJI} Question 3 {BOLT_EMOJI} \n{player}, what do you want to be remembered as? \nA: Intelligent. \nB: Brave. \nC: Ambitious. \nD: Caring.")

    answer: str = input("Answer: ")
    valid_answer: bool = False
    while valid_answer is False:
        # Ravenclaw
        if answer == "A":
            points += 2
            valid_answer = True
        # Gryffindor
        elif answer == "B":
            points += 3
            valid_answer = True
        # Slytherin
        elif answer == "C":
            points += 4
            valid_answer = True
        # Hufflepuff
        elif answer == "D":
            points += 1
            valid_answer = True
        else:
            answer = input("That wasn't an answer choice! Try again: ")


# Question 4
def question_4(points: int) -> int:
    """Question 4 of quiz."""
    global player
    print(f"\n{BOLT_EMOJI} Question 4 {BOLT_EMOJI} \n{player}, what animal would you have as a pet? \nA: Owl. \nB: Cat. \nC: Toad. \nD: Snake.")

    answer: str = input("Answer: ")
    valid_answer: bool = False
    while valid_answer is False:
        # Ravenclaw
        if answer == "A":
            points += 2
            valid_answer = True
        # Gryffindor
        elif answer == "B":
            points += 3
            valid_answer = True
        # Hufflepuff
        elif answer == "C":
            points += 1
            valid_answer = True
        # Slytherin
        elif answer == "D":
            points += 4
            valid_answer = True
        else:
            answer = input("That wasn't an answer choice! Try again: ")
    return points


# Question 5
def question_5() -> None:
    """Question 5 of quiz."""
    global points

    print(f"\n{BOLT_EMOJI} Question 5 {BOLT_EMOJI} \nOut of these options, what is your favorite school subject? \nA: Mathematics. \nB: Science. \nC: History or Political Science. \nD: English Literature.")

    answer: str = input("Answer: ")
    valid_answer: bool = False
    while valid_answer is False:
        # Gryffindor 
        if answer == "A":
            points += 3
            valid_answer = True
        # Slytherin
        elif answer == "B":
            points += 4
            valid_answer = True
        # Hufflepuff
        elif answer == "C":
            points += 1
            valid_answer = True
        # Ravenclaw
        elif answer == "D":
            points += 2
            valid_answer = True
        else:
            answer = input("That wasn't an answer choice! Try again: ")


# FATE
def fate() -> None:
    """Generates a random number of points to add to players score for 'fate'."""
    global points

    input(f"\n{BOLT_EMOJI} FATE {BOLT_EMOJI} \nThis last part is up to fate! All you have to do is press enter and the sorting hat will choose your destiny.")
    
    from random import randint
    sorting_hat: int = randint(1, 4)

    if sorting_hat == 1:
        points += 1
    elif sorting_hat == 2:
        points -= 1
    elif sorting_hat == 3:
        points += 2
    else:
        points -= 2


# End results prints what house player is based on where their adventure points lie
def resulting_house() -> str:
    """Determines what house player is based on how many adventure points they have."""
    global points

    house: str = ""
    if points >= 1 and points <= 6:
        house = "HUFFLEPUFF"
    elif points >= 7 and points <= 12:
        house = "RAVENCLAW"
    elif points >= 13 and points <= 18:
        house = "GRYFFINDOR"
    elif points >= 19 and points <= 26:
        house = "SLYTHERIN"
    return house

        
if __name__ == "__main__":
    main()