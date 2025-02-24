# a welcome banner that can be tailored to any game
def create_welcome_page(game_name):
    """
    This function creates a welcome banner.
    :param game_name: Name of the game being played (str).
    :return: A formatted banner (str)
    """
    welcome_line = f"{"#" * 61}\n"
    space = f"{"#" * 4} {" " * 51} {"#" * 4}\n"
    game_interface = f"Let's play {game_name}!"
    game_interface_line = f"{"#" * 4} {game_interface.center(52)}{"#" * 4}\n"
    welcome_page = f"{welcome_line}{space}{game_interface_line}{space}{welcome_line}"
    return welcome_page


# a general function that prompts the user to play again
# this function has three parameters with default values for the prompt, yes_options and no_options
def play_again(prompt="\nDo you want to play again? (yes/no): ",
               yes_options=("yes", "y"),
               no_options=("no", "n")):
    """
    This function asks the user if they want to play again and only stops when it receives a valid response.
    :param prompt: The question shown to the user (str).
    :param yes_options: Responses considered as "yes" (tuple).
    :param no_options: Responses considered as "no" (tuple).
    :return: True if the user wants to play again, False otherwise (bool).
    """

    # a while loop that will keep asking the question until a valid answer is given
    while True:
        # displays the prompt and requires user's input
        # strip removes any extra spaces at the beginning or end
        # lower method converts the input to lowercase so there's no inconsistency in case
        answer = input(prompt).strip().lower()

        # if the user's answer is within the yes options, the function returns True (the user wants to play again)
        if answer in yes_options:
            return True

        # if the user's answer is within the no options, the function returns False (the user doesn't want to play again)
        elif answer in no_options:
            return False

        # any other input will be considered invalid
        else:
            print("Invalid input. Please try again.")


# this block ensures that the code inside it only runs when the script is executed directly -- and not when it's imported as a module in another script
# the code inside the block will only be run in another file if we import the module and call these specific functions
# it also allows us to test specific functions within this file by running it as a script
if __name__ == "__main__":
    display_banner = create_welcome_page("Rock, Paper, Scissors")
    print(display_banner)