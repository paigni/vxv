import sys
import time

from service import update_count, first_team, second_team
from interface import start_game


def main():
    start_game()
    first_team_hero = -1
    second_team_hero = -1

    while True:
        first_hero = first_team[first_team_hero]
        second_hero = second_team[second_team_hero]
        if not first_hero.current_hp <= 0:
            first_team_hero = update_count(first_team, first_team_hero)
        else:
            print(f'Умер {first_hero.name},игрок первой команды')
            first_team.remove(first_hero)
            if not first_team:
                sys.exit("Победила вторая команда")
            else:
                first_team_hero = update_count(first_team, first_team_hero)

        if not second_hero.current_hp <= 0:
            second_team_hero = update_count(second_team, second_team_hero)
        else:
            print(f'Умер {second_hero.name},игрок второй команды')
            second_team.remove(second_hero)
            if not second_team:
                sys.exit("Победила первая команда")
            else:
                second_team_hero = update_count(second_team, second_team_hero)

        print("Первая команда нанесла урон:")
        first_hero.hero_damage(second_hero)
        time.sleep(0.1)

        print("Вторая команда нанесла урон:")
        second_hero.hero_damage(first_hero)
        time.sleep(0.1)


if __name__ == '__main__':
    main()
