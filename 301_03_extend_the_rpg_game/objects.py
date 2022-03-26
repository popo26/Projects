import random
import sys

class Hero:
    def __init__(self):
        self.name = "Hero"
        self.level = 3
        self.strength = 3

    def attack(self):
        attack_list = ["punch", "kick", "stab"]
        attack_choice = random.choice(attack_list)
        print(f"\n🦸🦸🦸🦸🦸Hero {attack_choice}s.🦸🦸🦸🦸🦸")
        
    def run_away(self):
        if self.level == 0:
            print(f"Hero's level is below {self.level}. GAME OVER")
            sys.exit()
        else:
            self.level -= 1
            print(f"\n🏃🏃🏃Hero runs away. 🏃🏃🏃\nHero's current strengh: {self.strength}\ncurrent level:{self.level}")

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
        
    def win_lose(self, opponent):
        dice = [1,2,3,4,5,6]
        random_dice_throw = random.choice(dice)
        if self.strength == 0 or self.level == 0:
            if self.strength == 0:
                print(f"\nHero strength is below {self.strength}.\nHero level is {self.level}. GAME OVER.")
                sys.exit()
            elif self.level == 0:
                print(f"\nHero strength is {self.strength}.\nHero level is below {self.level}. GAME OVER.")
                sys.exit()
        elif self.level < opponent.ene_level:
            self.level -= 1
            self.strength -= 1
            print("Hero lost.")   
            print(f"Hero strength: {self.strength}\nHero level: {self.level}")
        elif self.level == opponent.ene_level:
            print("Tie. Let's throw a dice")
            if random_dice_throw < 3:
                if (opponent.ene_strength - self.strength <= 2) and (opponent.ene_strength == 10):
                    self.level += 2
                    self.strength += 2
                elif self.strength > opponent.ene_strength:
                    self.level += 1
                    self.strength += 1
                print("Hero won!")
                print(f"Hero strength: {self.strength}\nHero level: {self.level}")
            elif random_dice_throw >= 3:
                if (opponent.ene_strength - self.strength <= 2) and (opponent.ene_strength == 10):
                    self.level -= 2
                    self.strength -= 2
                elif self.strength < opponent.ene_strength:
                    self.level -= 1
                    self.strength = -1
                print("Hero lost.")
                print(f"Hero strength: {self.strength}\nHero level: {self.level}")
        elif self.level > opponent.ene_level:
                self.level += 1
                self.strength += 1
                print("Hero won!")
                print(f"Hero strength: {self.strength}\nHero level: {self.level}")


class Opponent:
    def __init__(self, name, strength, level):
        self.name = name
        # global extent
        self.ene_strength = strength
        self.ene_level = level

    def attack(self):
        attack_list = ["throw", "shake", "smash"]
        attack_choice = random.choice(attack_list)
        if attack_choice == "smash":
            print(f"\n!!!!!!{self.name} {attack_choice}es Hero.!!!!!")
        else:
            print(f"\n!!!!!!{self.name} {attack_choice}s Hero.!!!!!!")

    def __str__(self):
        return "😈ENEMY😈"

class WeekOpponent(Opponent):

    def attack(self):
        attack_list = ["tickle", "hops on Hero's back", "slap"]
        attack_choice = random.choice(attack_list)
        if attack_choice == "hops on Hero's back":
            print(f"\n::::::{self.name} {attack_choice}.::::::")
        else:
            print(f"\n::::::{self.name} {attack_choice}s Hero.::::::")

    def __str__(self):
        return "🤡WEAK ENEMY🤡"

class FinalBoss(Opponent):
    
    def __init__(self, name, strength, level):
        super().__init__(name, strength, level)
        self.name = "Boss" + " " + name
        self.trick = getattr
        

    def boss_trick(self):
        trick_list = ["hypnotize", "makes Hero disappear", "goes into Hero's body"]
        self.attack_choice = random.choice(trick_list)
        if self.attack_choice == "hipnotize":
            print(f"\n🗡️🗡️🗡️{self.name} {self.attack_choice}s Hero.🗡️🗡️🗡️")
        else:
            print(f"\n🗡️🗡️🗡️{self.name} {self.attack_choice}.🗡️🗡️🗡️")

    def __str__(self):
        return "👹FINAL BOSS👹"

if __name__ == "__main__":
    opponent = Opponent()




    
