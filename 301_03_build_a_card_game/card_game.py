#Old Maid

from cards import Player, PlayGame
import sys
import webbrowser

is_on = True

num_players = int(input("\nHow many players?: "))
if num_players > 20:
    print("Let's just not play. Too many people. It's borning🥱")
    sys.exit()
elif num_players == 1:
    print("Do you have a friend? Find at least one and come back play😉")
    sys.exit()
elif num_players < 1:
    print("How do you play without player?\nHave a read here🧐. See you soon!")
    reference = "https://bicyclecards.com/how-to-play/old-maid/"
    webbrowser.open(reference)
    sys.exit()

player_list = []
for i in range(0, num_players):
    name = f"player{i}"
    x = Player(name)
    player_list.append((str(x)))

for i in range(len(player_list)):
    print(f"Player name: {player_list[i].capitalize()} ♠️♠️♠️♠️♠️ Player number: {i}.")

game = PlayGame(num_players)

game.shuffle_cards()
game.split_cards(num_players)
game.allocate_cards(*player_list)
game.tidy_up_cards()

while is_on:
    game.pick_card(*player_list)
    game.tidy_up_cards()
    






