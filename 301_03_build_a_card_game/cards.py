import random

class Player:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class PlayGame:
    def __init__(self, num_players):
        self.cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "K" ]
        self.num_players = num_players
        self.final_all_cards = []

    def shuffle_cards(self):
        random.shuffle(self.cards)
        print(self.cards)

    def split_cards(self, num_players):
        step = 51 // num_players
        # print(step)
        all_cards = []
        for i in range(0, len(self.cards), step):
            chunk = []
            chunk.append(self.cards[i:i+step])
            all_cards.append(chunk)

        if len(all_cards) > num_players:
            last_chunk = all_cards.pop(-1)[0]
            for i in range(len(last_chunk)):
                for index in range(len(all_cards)):
                    if last_chunk == []:
                        break
                    else:
                        all_cards[index][0].append(last_chunk[0])
                        last_chunk.remove(last_chunk[0])

        self.final_all_cards = []
        for i in range(len(all_cards)):
            self.final_all_cards.append(all_cards[i][0])
        print(self.final_all_cards)

    def allocate_cards(self, *args):
        self.players_cards = {}
        for i in range(len(args)):
            self.players_cards[args[i]] = self.final_all_cards[i]
        print("\n")
        print(self.players_cards)

    def tidy_up_cards(self, **kwargs):
        for v in self.players_cards.values():
            for card in v:
                pass
                

    def pick_card(self, player_num, *args):
        print("\n")
        print("Pick a card from next player.")
        # player_num = input("What is your name? e.g. 'player1': ")
        #A player picks one card from next player and remove the card from next player
        self.players_cards[args[player_num]].append(self.players_cards[args[player_num + 1]][0])
        self.players_cards[args[player_num + 1]].remove(self.players_cards[args[player_num + 1]][0])
        print(self.players_cards)


    def win_lose(self):
        pass


        
# if __name__ == "__main__":
#     player_list = Player()
#     num_player = Player()



