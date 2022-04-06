from objects_301_06 import Hero, Opponent
import random

is_game_on = True

hero = Hero()
enemy1 = Opponent(1, 1)
enemy2 = Opponent(2, 2)
enemy3 = Opponent(3, 3)
enemy4 = Opponent(4, 4)
enemy5 = Opponent(5, 5)
enemy6 = Opponent(6, 6)


while is_game_on:
    enemy_list = [enemy1, enemy2, enemy3, enemy4, enemy5, enemy6]
    random_enemy = random.choice(enemy_list)
    print(f"\nHero's current strength is {hero.strength}. level is {hero.level}.")
    print(f"There is an {random_enemy}. Strength: {random_enemy.strength}. Level: {random_enemy.level}")
    hero_choice = input("\nIs hero going to attack or run away?\n0 for attack\n1 for run away\n9 for quit: ")
    if hero_choice == "9":
        break
    elif hero_choice == "1":
        hero.run_away()
        hero.power()
    elif hero_choice == "0":
        hero.attack()
        hero.win_lose(random_enemy)
    else:
        print("I can't read. Try again.")


    
