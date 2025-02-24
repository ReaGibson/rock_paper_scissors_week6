# from game_functions import *

# import our two modules from our package and use * to call all functions within them
from game_functions.general_game_functions import *
from game_functions.rps_functions import *

# pass Rock Paper Scissors game parameter into the create_welcome_page function via a variable -- then print the banner
display_banner = create_welcome_page("Rock, Paper, Scissors")
print(display_banner)

# call the rounds function which incorporates the full rules of the game (user choice, computer choice, play round, three rounds + scoring)
rounds()

# call the replay function so the user can play again or exit the game
play_again_outcomes()

