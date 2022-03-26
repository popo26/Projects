
import random

class Pokemon():
    def __init__(self) -> None:
        self.name = input('What is your name?: ').capitalize()
        self.primary_type = ["water", "fire", "grass"]
        self.max_hp = 10 #hp=hit point
        self.hp = 3

    def battle(self):
        while True:
            #water > fire > grass > water
            print(f"\nYour turn, {self.name}!")
            user_choice = input("\nEnter 0 for Water, 1 for Fire, 2 for Grass.\n111 to feed more HP. \n999 to stop game: ").lower()
            battle_choices = [0, 1, 2]
            computer_choice = random.choice(battle_choices)
            if user_choice == "999":
                break
            elif user_choice == "111":
                self.feed()
            elif user_choice.isdigit():
                user_choice = int(user_choice)
                if user_choice > computer_choice and user_choice < 3:
                    if self.hp == self.max_hp:
                        print(f"You won. Computer choice is {self.primary_type[computer_choice].capitalize()}.")
                        print(f"You reached Max HP. Current HP: {self.hp}")
                    else:
                        self.hp += 1
                        print(f"You won. Computer choice is {self.primary_type[computer_choice].capitalize()}.")
                        print(f"Current HP: {self.hp}")
                elif user_choice < computer_choice and user_choice < 3:
                    self.hp -= 1
                    print(f"You lost. Computer choice is {self.primary_type[computer_choice].capitalize()}.")
                    print(f"Current HP: {self.hp}")
                    if self.hp == 0:
                        print("Your HP is 0. GAME OVER")
                        break
                elif user_choice == computer_choice:
                    print("Tie.") 
                    print(f"Current HP: {self.hp}")
                else:
                    print("I don't understand your choice. Try again.")
            else:
                print("I don't understand your choice. Try again.")

    def feed(self):
        if self.hp <= 6:
            self.hp += 3
            print(f"\nYour HP is regained by 3. Current HP is {self.hp}.")
        elif self.hp >= 7 and self.hp < 10 or self.hp == 9:
            self.hp +=1
            print(f"\nYour HP is regained by 1. Current HP is {self.hp}.")
        else:
            print(f"\nYour HP can't be regained at the moment. You already have Max HP {self.max_hp}.")

p = Pokemon()
p.battle()

