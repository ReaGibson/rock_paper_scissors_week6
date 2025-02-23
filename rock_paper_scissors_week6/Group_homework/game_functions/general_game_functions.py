def create_welcome_page(game_name):
    welcome_line = f"{"#" * 60}\n"
    space = f"{"#" * 5} {" " * 50} {"#" * 5}\n"
    game_interface = f"Let's play {game_name}!"
    game_interface_line = f"{"#" * 5} {game_interface.center(50)}{"#" * 5}\n"
    welcome_page = f"{welcome_line}{space}{game_interface_line}{space}{welcome_line}"
    return welcome_page

welcome_page = create_welcome_page('Rock, Paper, Scissors')


# def boxed_banner(game_name):
#     banner_width = 60
#     title = f"Welcome to {game_name}!"
#     top_border = "╔" + "═" * (banner_width - 2) + "╗"
#     bottom_border = "╚" + "═" * (banner_width - 2) + "╝"
#     empty_line = "║" + " " * (banner_width - 2) + "║"
#     title_line = "║" + title.center(banner_width - 2) + "║"
#     return f"{top_border}\n{empty_line}\n{title_line}\n{empty_line}\n{bottom_border}"


if __name__ == "__main__":
    display_banner = create_welcome_page("Rock, Paper, Scissors")
    print(display_banner)


def play_again(prompt="\nDo you want to play again? (yes/no): ",
               yes_options=("yes", "y"),
               no_options=("no", "n")):
    """
    Ask the user if they want to play again.

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





