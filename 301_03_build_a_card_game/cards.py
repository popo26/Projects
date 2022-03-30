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

    def tidy_up_cards(self):
        for card_set in self.players_cards.values():
            # print("\nOriginal V")
            # print(card_set)
            for item in card_set:
                card_set.sort()#Sort the list
                # print(f"Sorted: {card_set}")
                if card_set.count(item) > 1:
                    # print(f"\nDuplicate item: {item}")#Duplicate element
                    dup_item_index = card_set.index(item) # Find the location of the duplicate element
                    # print(dup_item_index)
                    card_set.remove(item) #Remove the duplicate element
                    '''Another half of the duplicate element falls into the location of the original duplicate element already removed.
                    Then remove it.'''
                    card_set.pop(dup_item_index) 
                else:
                    continue
                    # print("no, duplicate")
            # print(f"Final: {card_set}")
        print(f"\nPlayers' cards without duplicate: {self.players_cards}")   
                

    def pick_card(self, *args):
        print("\n")
        print("Pick a card from next player.")
        player_num = int(input("What is your player number?: "))
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



