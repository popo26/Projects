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
        players_cards = {}
        for player in args:
            for cards in self.final_all_cards:
                players_cards[player] = cards
        print(players_cards)

    def pick_card(self, player_num):
        print("Pick a card from next player.")
        # players_cards = 

        
# if __name__ == "__main__":
#     player_list = Player()
#     num_player = Player()



