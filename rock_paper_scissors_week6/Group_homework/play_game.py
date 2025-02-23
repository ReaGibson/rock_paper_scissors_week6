# from game_functions import *
from game_functions.general_game_functions import *
from game_functions.rps_functions import *

display_banner = create_welcome_page("Rock, Paper, Scissors")
print(display_banner)

rounds()

if play_again():
    print("Let's play again!")
    rounds()
else:
    print("Thanks for playing!")

