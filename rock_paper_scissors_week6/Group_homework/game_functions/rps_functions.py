# import the random module to use the random.choice method
import random

# a function to get the computer's choice from a list
def get_computer_choice():
    """
    This function randomly selects a choice for the computer from a  list.
    :return: Rock, Paper or Scissors (str).
    """
    # returns a random choice from a list
    return random.choice(['Rock', 'Paper', 'Scissors'])


# a function to get the user's choice from a dictionary
def get_user_choice():
    """
    This function prompts the user to enter a choice of R, P, S and ensures the input is valid.
    :return: Rock, Paper or Scissors (str).
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
    This function plays a single round of Rock, Paper, Scissors between a user and the computer.
    It gets both the user and the computer's choice, compares the choices to determine a winner, and prints the winner for each round.
    :return: The round's score for each of the user and computer (tuple).
    """

    # set the score for each round to zero as a baseline
    user_round_score = 0
    computer_round_score = 0

    # call the user_choice and computer_choice functions to capture user and computer selection -- assign these to variables so we can reuse
    user = get_user_choice()
    computer = get_computer_choice()

    # show the choices made by both the user and the computer
    print(f"You chose: {user}")
    print(f"The computer chose: {computer}")

    # use conditional logic to determine the winner of a round
    # draw if the user and computer pick the same thing
    if user == computer:
        print("This round is a draw\n")

    # these are the conditions which mean the user wins
    elif (user == "Rock" and computer == "Scissors") or \
        (user == "Paper" and computer == "Rock") or \
        (user == "Scissors" and computer == "Paper"):
        print("You win this round!\n")

        # if the user wins this round, their score for the round is set to 1
        user_round_score = 1

    # if none of the above conditions are met, then the computer wins
    else:
        print("You lose this round!\n")

        # if the computer wins this round, its score for the round is set to 1
        computer_round_score = 1

    # return a tuple containing the score for the round (user, computer)
    # this stores the result of the round and can be called later
    return user_round_score, computer_round_score


# function to repeat the round 3 times and calculate total score
def rounds():
    """
    This function plays three rounds of the game, tallies the score for the user and computer at the end, and prints the final result.
    :return: None.
    """

    # set the total user and computer scores to zero
    total_user_score = 0
    total_computer_score = 0

    # for loop runs three rounds; in each round it calls play_round (which itself returns two values: user's round score and computer's round score)
    for i in range(3):
        user_round_score, computer_round_score = play_round()
        # here the round scores are added to the total score (which was set to zero)
        total_user_score += user_round_score
        total_computer_score += computer_round_score

    # display the final score for the user and computer after three rounds
    print(f"The final score is:\nYou: {total_user_score}, Computer: {total_computer_score}")

    # conditional logic to determine the overall winner of the game after three rounds
    if total_user_score > total_computer_score:
        print("Congratulations, you win the game! 🤩")

    elif total_user_score == total_computer_score:
        print("It's a tie! Try again to beat the Computer 💪🏼")

    else:
        print("Computer won the game. Better luck next time! 😔")


# this block ensures that the code inside it only runs when the script is executed directly -- and not when it's imported as a module in another script
# the code inside the block will only be run in another file if we import the module and call these specific functions
# it also allows us to test specific functions within this file by running it as a script
if __name__ == '__main__':
    # testing that the get_user_choice function is working
    user = get_user_choice()
    print(user)