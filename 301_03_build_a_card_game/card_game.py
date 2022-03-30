#Old Maid

from re import I
from cards import Player, PlayGame

num_players = int(input("How many players?: "))

player_list = []
for i in range(0, num_players):
    name = f"player{i}"
    x = Player(name)
    player_list.append(x)
print(player_list)

# player = Player("Player1")
# print(player)
# player.player_list()

game = PlayGame(num_players)
game.shuffle_cards()

game.split_cards(num_players)

# players_cards = {}
# for player in player_list:
#     for cards in game.final_all_cards:
#         players_cards[player] = cards
# print(players_cards)

game.allocate_cards(*player_list)





