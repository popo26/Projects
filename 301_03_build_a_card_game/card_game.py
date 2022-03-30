#Old Maid

from re import I
from cards import Player, PlayGame

num_players = int(input("How many players?: "))

player_list = []
for i in range(0, num_players):
    name = f"player{i}"
    x = Player(name)
    player_list.append((str(x)))
print(player_list)

# player = Player("Player1")
# print(player)
# player.player_list()

game = PlayGame(num_players)
game.shuffle_cards()

game.split_cards(num_players)

game.allocate_cards(*player_list)

game.pick_card(0, *player_list)

# print(player_list[0])





