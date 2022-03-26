import random
import sys

class Hero():
    def __init__(self):
        self.name = "Hero"
        self.level = 1
        self.strength = 1

    def attack(self):
        attack_list = ["punch", "kick", "stab"]
        attack_choice = random.choice(attack_list)
        print(f"\nHero {attack_choice}s.")
        
    def run_away(self):
        if self.level == 0:
            print(f"Hero's level is below {self.level}. GAME OVER")
            sys.exit()
        else:
            self.level -= 1
            print(f"\nHero runs away. \nHero's current strengh: {self.strength}\ncurrent level:{self.level}")

    def power(self):
        power_list = ["food", "sleep", "drink"]
        choice = random.choice(power_list)
        if choice == "food":
            self.strength += 1
            print(f"\nHero gained strength by eating some food.\nStrength: {self.strength}\nLevel: {self.level}")
        elif choice == "sleep":
            self.strength += 1
            self.level += 1
            print(f"\nHero gained strength and level from sleep.\nStrength: {self.strength}\nLevel: {self.level}")
        else:
            print("\nHero was thirsty. He had some drink.")
        
    def win_lose(self, other):
        dice = [1,2,3,4,5,6]
        random_dice_throw = random.choice(dice)
        if self.strength == 0 or self.level == 0:
            if self.strength == 0:
                print(f"\nHero strength is below {self.strength}.\nHero level is {self.level}. GAME OVER.")
                sys.exit()
            elif self.level == 0:
                print(f"\nHero strength is {self.strength}.\nHero level is below {self.level}. GAME OVER.")
                sys.exit()
        elif self.level < other.level:
            self.level -= 1
            self.strength -= 1
            print("Hero lost.")   
            print(f"Hero strength: {self.strength}\nHero level: {self.level}")
        elif self.level == other.level:
            print("Tie. Let's throw a dice")
            if random_dice_throw < 3:
                self.level += 1
                self.strength += 1
                print("Hero won!")
                print(f"Hero strength: {self.strength}\nHero level: {self.level}")
            elif random_dice_throw >= 3:
                self.level -= 1
                self.strength -= 1
                print("Hero lost.")
                print(f"Hero strength: {self.strength}\nHero level: {self.level}")
        elif self.level > other.level:
                self.level += 1
                self.strength += 1
                print("Hero won!")
                print(f"Hero strength: {self.strength}\nHero level: {self.level}")


class Opponent():
    def __init__(self, strength, level):
        self.strength = strength
        self.level = level

    def __str__(self):
        return "😈ENEMY😈"

    
