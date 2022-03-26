# Rock-Paper-Scissors Game
# Code a game of rock paper scissors.

# Instructions
# take in a number 0-2 from the user that represents their hand
# generate a random number 0-2 to use for the computer's hand
# call the function get_hand to get the string representation of the user's hand
# call the function get_hand to get the string representation of the computer's hand
# call the function determine_winner to figure out who won
# print out the player hand and computer hand
# print out the winner
# Some Tips
# Creating a function that gets a "hand" based on a number.

# The function should take in a number and return the string representation of the hand. E.g.:

# def get_hand(hand):
#     # 0 = scissor, 1 = rock, 2 = paper

#     # for example if the variable hand is 0, it should return the string "scissor"
#     pass

import random

user_hand= int(input("Rock(0), Scissor(1), Paper(2): "))
computer = [0, 1, 2]
choices = ["Rock", "Scissor","Paper"]
computer_hand = int(random.choice(computer))
print(computer_hand)

def get_hand(hand):
    if hand == 0:
        print("Your hand is Rock")
    elif hand == 1:
        print("Your hand is Scissor")
    elif hand == 2:
        print("Your hand is Paper")
    else:
        print("I can't read you. Try again")
    print(f"Computer hand is {choices[computer_hand]}")

def determine_winner(hand, computer_choice):
    if hand == computer_choice:
        print("Tie")
    elif hand > computer_choice:
        print("you lost. The winner is Computer.")
    else:
        print("you win!")
      

get_hand(user_hand)
determine_winner(user_hand, computer_hand)

