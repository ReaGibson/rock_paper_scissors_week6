# from game_functions import *
from game_functions.general_game_functions import *
from game_functions.rps_functions import *

welcome_page = create_welcome_page('Rock, Paper, Scissors')
print(welcome_page)

# use a for loop to play 3 rounds of the game
for item in range(3):
    play_round()
