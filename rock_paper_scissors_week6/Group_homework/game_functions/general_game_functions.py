from game_functions.rps_functions import *

# a welcome banner that can be tailored to any game
def create_welcome_page(game_name):
    """
    This function creates a welcome banner
    :param game_name: str
    :return: str
    """
    welcome_line = f"{"#" * 61}\n"
    space = f"{"#" * 4} {" " * 51} {"#" * 4}\n"
    game_interface = f"Let's play {game_name}!"
    game_interface_line = f"{"#" * 4} {game_interface.center(52)}{"#" * 4}\n"
    welcome_page = f"{welcome_line}{space}{game_interface_line}{space}{welcome_line}"
    return welcome_page


# a general function that prompts the user to play again
# this function has three parameters with default values for prompt, yes_options and no_options
def play_again(prompt="\nDo you want to play again? (yes/no): ",
               yes_options=("yes", "y"),
               no_options=("no", "n")):
    """
    This function asks the user if they want to play again.

    Parameters:
        prompt (str): The question displayed to the user.
        yes_options (tuple): Accepted responses for "yes".
        no_options (tuple): Accepted responses for "no".

    Returns:
        bool: True if the user wants to play again, False otherwise.
    """

    while True:
        answer = input(prompt).strip().lower()
        if answer in yes_options:
            return True

        elif answer in no_options:
            return False

        else:
            print("Invalid input. Please try again.")


# a function to action the user's choice to play again or not
def play_again_outcomes():
        if play_again():
            print("Let's play again!")
            rounds()
        else:
            print("Thanks for playing!")


#
if __name__ == "__main__":
    display_banner = create_welcome_page("Rock, Paper, Scissors")
    print(display_banner)
    play_again_outcomes()

