
####Pseudocode from 101##############

# Build a CLI RPG game following the instructions from the course.
# Ask the player for their name.
# Display a message that greets them and introduces them to the game world.
# Present them with a choice between two doors.
# If they choose the left door, they'll see an empty room.
# If they choose the right door, then they encounter a dragon.
# In both cases, they have the option to return to the previous room or interact further.
# When in the seemingly empty room, they can choose to look around. If they do so, they will find a sword.
# They can choose to take it or leave it.
# When encountering the dragon, they have the choice to fight it.
# If they have the sword from the other room, then they will be able to defeat it and win the game.
# If they don't have the sword, then they will be eaten by the dragon and lose the game

########Pseudocode from 201#############

# Save the user input options you allow e.g. in a set that you can check against when your user makes a choice.
# Create an inventory for your player, where they can add and remove items.
# Players should be able to collect items they find in rooms and add them to their inventory.
# If they lose a fight against the dragon, then they should lose their inventory items.
# Add more rooms to your game and allow your player to explore.
# Some rooms can be empty, others can contain items, and yet others can contain an opponent.
# Implement some logic that decides whether or not your player can beat the opponent depending on what items they have in their inventory
# Use the random module to add a multiplier to your battles, similar to a dice roll in a real game. This pseudo-random element can have an effect on whether your player wins or loses when battling an opponent.

##Ai: Improvement from 101 project is:
##1, It can keep playing
##2, More rooms, more armor choices, more dragons.

inventory = {"sword": 0, "axe": 0}
life = 0
rooms = ["sword", "empty", "empty", "dragon", "sword", "axe", "two_dragons"]
is_on = True

def greeting():
    user_name = input("What is your name?: ").lower()
    print(f"Welcome {user_name.capitalize()} to the game world! ")
    print(
        f"Current life is {life}. Now you have {inventory['sword']} swords and {inventory['axe']} axes.")

def empty_room():
    print("\nIt's a empty room. Let's go back to the previuos room.")
    select_door()

def play_or_quit():
    global is_on
    user_input = input("\nTo keep playing press 0. To quit, enter 'quit'.: ")
    if user_input == "quit":
        is_on == False
    elif user_input == "0":
        restart()
    else:
        print("I can't read. Try again.")
        select_door()

def life_zero_choice():
    global is_on
    user_choice = input(f"You still have {life} life. Would you like to play again? 'Yes' to continue or 'Quit' to stop:").lower()
    if user_choice == "quit":
        is_on == False
    elif user_choice == "yes":
        restart()
    else:
        print("I can't read. Try again.")
        select_door()

def select_door():
    user_door_choice = int(
        input("\nThere are 7 doors. Which one would you like to open? Enter 0 - 6: "))
    print(user_door_choice)
    if user_door_choice == 1 or user_door_choice == 2:
        empty_room()
    elif user_door_choice == 3:
        dragon_room1()
    elif user_door_choice == 6:
        dragon_room2()
    elif user_door_choice == 0 or user_door_choice == 4 or user_door_choice == 5:
        if user_door_choice == 0 or user_door_choice == 4:
                inventory["sword"] += 1
                print(
                    f"There is a sword. Your armor is now {inventory['sword']} swords and {inventory['axe']} axes.")
                print(inventory)
                print("Now let's go back to the previous room.")
                select_door()
        elif user_door_choice == 5:
                inventory["axe"] += 1
                print(
                    f"There is an axe. Your armor is now {inventory['sword']} swords and {inventory['axe']} axes.")
                print(inventory)
                print("Now let's go back to the previous room.")
                select_door()
        else:
                print("I can't read. Try again.")
                select_door()
    else:
        print("Not sure what you entered. Try again.")
        select_door()

def dragon_room1():
    global is_on, life
    print(
        f"\nThere is a dragon. You have {inventory['sword']} swords and {inventory['axe']} axes.")
    user_choice = input(
        "Are you going to fight 'Yes' or go back to the previous room 'No'? : ").lower()
    if user_choice == "no":
        select_door()
    elif user_choice == 'yes':
        if inventory["sword"] >= 1 or inventory["axe"] > 0:
            print("You killed the dragon.")
            life += 1
            play_or_quit()
        elif inventory["sword"] > 0 or inventory["axe"] >= 1:
            life += 1
            play_or_quit()
        elif inventory["sword"] == 0 or inventory["axe"] == 1:
            print("You are beaten.")
            life -= 1
            if life > 1:
                life_zero_choice()
            else:
                print("GAME OVER")
                is_on = False
    else:
        print("Sorry I can't read. Try again.")
        dragon_room1()

def dragon_room2():
    global is_on, life
    print(f"\nThere are 2 dragons. You have {inventory['sword']} swords and {inventory['axe']} axes.")
    user_choice = input(
        "Are you going to fight 'Yes' or go back to the previous room 'No'? : ").lower()
    if user_choice == "no":
        select_door()
    elif user_choice == 'yes':
        if (inventory["sword"] >= 2 and inventory["axe"] >= 0) or (inventory["sword"] >= 0 and inventory["axe"] >= 2) or (inventory["sword"] >= 1 and inventory["axe"] >= 1):
            print("You killed the dragon.")
            life += 1
            play_or_quit()
        elif (inventory["sword"] < 2 and inventory["axe"] == 0) or (inventory["sword"] == 0 and inventory["axe"] < 2):
            print("You are beaten.")
            life -= 1
            if life > 1:
                life_zero_choice()
            else:
                print("GAME OVER")
                is_on = False
    else:
        print("\nSorry I can't read. Try again.")
        dragon_room2()

def restart():
    print(f"Welcome back. You currently have:\n{life} lives\n{inventory['sword']} swords\n{inventory['axe']} axes")
    select_door()


greeting()
select_door()


####code from 101####

# is_game_on = True
# sword = 0
# life = 1
# user_name = input("What is your name?: ").lower()
# print(f"Welcome {user_name.capitalize()} to the game world! ")
# door_choice = input("left or right, which door would you like?: ").lower()
# print(f"Current life is {life}. sword is {sword}")

# while is_game_on:
#     if door_choice == "left":
#         return_choice = input("It's a empty room. Would you like to go back to the previous room? Yes or No: ").lower()
#         if return_choice == "yes":
#             door_choice = input("left or right, which door would you like?: ").lower()
#         else:
#             sword_choice = input("Look around. There is a sword. Would you like to TAKE IT or LEAVE IT?: ")
#             if sword_choice == "take it":
#                 sword += 1
#                 print("Now you have 1 sword.")
#                 print(f"Current life is {life}. sword is {sword}")
#             elif sword_choice == "leave it":
#                 print("OK.")
#                 door_choice = input("left or right, which door would you like?: ").lower()
#             elif sword_choice != "take it" or "leave it":
#                 sword_choice2 = input("Sorry I don't understand. enter 'LEAVE IT' or 'TAKE IT':" )
#                 if sword_choice2 == "take it":
#                     sword += 1
#                     print("Now you have 1 sword.")
#                 elif sword_choice2 == "leave it":
#                     print("OK.")
#                     door_choice = input("left or right, which door would you like?: ").lower()

#     elif door_choice == 'right':
#         return_choice = input("There is a dragon! Woudl you like to go back to the previuos room? Yes or No: ").lower()
#         if return_choice == "yes":
#             door_choice = input("left or right, which door would you like?: ").lower()
#         elif return_choice == "no":
#             fight_choice = input("Are you gonna fight with the dragon?: ").lower()
#             if fight_choice == 'yes':
#                 if sword >= 1:
#                     print("You killed the dragon!")
#                     life += 1
#                     print(f"Current life is {life}. sword is {sword}")
#                     is_game_on = False
#                     # another_try = input(f"You eared a new life. Now your life is {life}.\nWould you like to try again?: ").lower()
#                     # if another_try == "yes":
#                     #     print(user_name)
#                     #     print(f"Current life is {life}. sword is {sword}")
#                     # else:
#                     #     is_game_on = False

#                 if sword == 0:
#                     print("You lost since you don't have any sword")
#                     life -= 1
#                     print(f"Current life is {life}. sword is {sword}")
#                     if life >= 1:
#                         print(f"You have {life} life left. Try again.\n{user_name}")
#                     else:
#                         is_game_on = False

#             elif fight_choice == 'no':
#                 door_choice = input("left or right, which door would you like?: ").lower()
