def create_welcome_page(game_name):
    welcome_line = f"{"#" * 60}\n"
    space = f"{"#" * 5} {" " * 50} {"#" * 5}\n"
    game_interface = f"Let's play {game_name}!"
    game_interface_line = f"{"#" * 5} {game_interface.center (50)} {"#" * 5}\n"
    welcome_page = f"{welcome_line}{space}{game_interface_line}{space}{welcome_line}"
    return welcome_page
