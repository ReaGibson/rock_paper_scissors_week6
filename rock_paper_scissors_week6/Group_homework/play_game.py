# from game_functions import *

# import our two modules from our package and use * to call all functions within them
from game_functions.general_game_functions import *
from game_functions.rps_functions import *

# pass Rock Paper Scissors game parameter into the create_welcome_page function via a variable -- then print the banner
display_banner = create_welcome_page("Rock, Paper, Scissors")
print(display_banner)

# call the rounds function which incorporates the full rules of the game (user choice, computer choice, play round, three rounds + scoring)
rounds()

# a for loop that determines what happens in response to the user's choice in play_again
# if the result of the play_again function is True, it prints a message and then calls the rounds function to start a new round of the game
if play_again():
    print("\nLet's play again!")
    rounds()

# otherwise (i.e., if the result of play_again is False), it prints a message and ends the game
else:
    print("\nThanks for playing!")