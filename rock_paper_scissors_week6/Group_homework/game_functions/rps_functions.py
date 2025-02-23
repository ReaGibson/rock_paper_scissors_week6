import random

def get_computer_choice():
    """
    This function randomly selects a choice for the computer
    :return: str.
    """
    return random.choice(['Rock', 'Paper', 'Scissors'])

def get_user_choice():
    """
    This function prompts the user to enter a choice of R, P, S and ensures the input is valid
    :return: str.
    """
    # use a dictionary to list all possible choices, matching Rock, Paper, Scissors to R, P or S
    possible_choices = {"R": "Rock", "P": "Paper", "S": "Scissors"}

    # prompts the user for input -- use .upper to convert input to uppercase for consistency
    user_input = input("Enter R for Rock, P for Paper, or S for Scissors: ").upper()

    # the while loop ensures the user enters a valid choice (preventing a key error)
    while user_input not in possible_choices:
        print("Invalid choice; please enter R, P, or S.")
        user_input = input("Enter R for Rock, P for Paper, or S for Scissors: ").upper()

    # this returns the full name of the user's choice, which is R, P or S
    return possible_choices[user_input]

def play_round():
    """
    This function plays a single round of Rock, Paper, Scissors between a user and the computer
    It gets both the user and the computer's choice, compares the choices to determine a winner, updating the scores accordingly and printing the result for each round
    :return: str
    """

    # call the user_choice and computer_choice functions within the play_round function -- so that this happens for each round
    # had this outside of play_round before and it wasn't being considered when I ran the for loop to run 3 rounds of the game :(
    user = get_user_choice()
    computer = get_computer_choice()

    # show the choices made by both the user and the computer
    print(f"You chose: {user}")
    print(f"The computer chose: {computer}")

    # use conditional logic to determine the winner of each round
    # draw if the user and computer pick the same thing
    if user == computer:
        print("This round is a draw\n")

    # these are the conditions which mean the user wins
    elif (user == "Rock" and computer == "Scissors") or \
        (user == "Paper" and computer == "Rock") or \
        (user == "Scissors" and computer == "Paper"):

        print("You win this round!\n")

    # if none of the above conditions are met, then the computer wins
    else:
        print("You lose this round!\n")

for item in range(3):
    play_round()




