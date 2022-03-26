from objects import FinalBoss, Hero, Opponent, WeekOpponent
import random

is_game_on = True

hero = Hero()
#Normal level enemies
enemy1 = Opponent("Tam",3 ,3)
enemy2 = Opponent("Tim",3, 4)
enemy3 = Opponent("Tum",4, 3)
enemy4 = Opponent("Tem",4, 4)
enemy5 = Opponent("Tom",5, 5)
enemy6 = Opponent("Teem",6, 6)
#Weak level enemies
enemy7 = WeekOpponent("Jim",1, 1)
enemy8 = WeekOpponent("Jam",1, 1)
enemy9 = WeekOpponent("Jem",1, 1)
#Boss level enemies
enemy10 = FinalBoss("Jumbo",10, 10)
enemy11 = FinalBoss("Gigante",10, 10)

while is_game_on:
    enemy_list = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6]
    week_enemy_list = [enemy7, enemy8, enemy9]
    boss_enemy_list = [enemy10, enemy11]
    no_boss_ememy_list = enemy_list + week_enemy_list
    random_enemy = random.choice(no_boss_ememy_list)
    if hero.level > 5 and hero.strength > 5:
        stronger_enemy_list = enemy_list + boss_enemy_list
        random_enemy = random.choice(stronger_enemy_list)
    print(f"\nHero's current strength is {hero.strength}. level is {hero.level}.")
    print(f"There is an {random_enemy}. Strength: {random_enemy.ene_strength}. Level: {random_enemy.ene_level}." )
    hero_choice = input("\nIs hero going to attack or run away?\n0 for attack\n1 for run away\n9 for quit: ")
    if hero_choice == "9":
        break
    elif hero_choice == "1":
        hero.run_away()
        hero.power()
    elif hero_choice == "0":
        hero.attack()
        random_enemy.attack()
        hero.win_lose(random_enemy)
    else:
        print("I can't read. Try again.")

