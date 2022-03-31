#Old Maid

from cards import Player, PlayGame


is_on = True

num_players = int(input("How many players?: "))

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
    






