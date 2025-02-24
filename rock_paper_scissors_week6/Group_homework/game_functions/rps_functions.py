# import the random module to use the random.choice method
import random

# a function to get the computer's choice from a list
def get_computer_choice():
    """
    This function randomly selects a choice for the computer from a  list
    :return: str
    """
    # returns a random choice from a list
    return random.choice(['Rock', 'Paper', 'Scissors'])


# a function to get the user's choice from a dictionary
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

    # returns the full name of the user's choice based on the dictionary
    return possible_choices[user_input]


# a function to play one round of the game
def play_round():
    """
    This function plays a single round of Rock, Paper, Scissors between a user and the computer
    It gets both the user and the computer's choice, compares the choices to determine a winner, and prints the winner for each round
    :return: str
    """

    # set the score for each round to zero as a baseline
    user_round_score = 0
    computer_round_score = 0

    # call the user_choice and computer_choice functions using variables, so we can use them again
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
        # if the user wins this round, their score for the round is 1
        user_round_score = 1

    # if none of the above conditions are met, then the computer wins
    else:
        print("You lose this round!\n")
        # if the computer wins this round, its score for the round is 1
        computer_round_score = 1

    # return a round score for the user and for the computer
    return user_round_score, computer_round_score



# function to repeat the round 3 times and calculate total score
def rounds():
    """

    :return:
    """
    # Initialise overall scores
    total_user_score = 0
    total_computer_score = 0

    for i in range(3):
        user_round_score, computer_round_score = play_round()
        total_user_score += user_round_score
        total_computer_score += computer_round_score

    print(f"The final score is:\nYou: {total_user_score}, Computer: {total_computer_score}")

    if total_user_score > total_computer_score:
        print("Congratulations, you win the game! 🤩")

    elif total_user_score == total_computer_score:
        print("It's a tie! Try again to beat the Computer 💪🏼")

    else:
        print("Computer won the game. Better luck next time! 😔")


if __name__ == '__main__':
    play_round()
    rounds()