import sys
import time

from service import spawn_characters, team_building, first_team, second_team
from check import check_choice, check_hero_hp, check_max_count
from collections import Counter
from hero_class import Hero


def show_heroes():
    """
        Выводит список героев доступных на текущий момент
    """
    print("Вам доступны следующие герои:\n")
    count = 0
    for hero in spawn_characters():
        count += 1
        print(f"{count}){hero.name}: здоровье {hero.max_hp} \n"
              f"урон {hero.damage}, и шанс попадания {hero.damage_chance}")


def team_view(team: list):
    team = Counter(team)
    for key, value in team.items():
        print(f"{key.name}-{value}")


def start_game():
    """
    Функция начала игры

    Returns:
        Ввод пользователя
    """
    use_input = 'd'
    while use_input != '1' and use_input.isdigit():
        use_input = input(f'Добро пожаловать в игру, чтобы начать нажмите 1\n'
                          f'для того чтобы выйти нажмите 2\n')
        if use_input == '1':
            break
        if use_input == '2':
            sys.exit("Вы завершили игру")

    while True:
        user_input = int(input("Выберите сторону для выбора персонажей \n "
                               "1-Первая команда \n 2-Вторая команда\n 3-Начать игру\n"))
        if user_input == 3:
            if first_team == [] or second_team == []:
                print("Для начала игры нужно добавить героев в обе команды")
                continue
            else:
                print("Игра началась")
                break
        elif user_input == 1 or user_input == 2:
            print("Выбор персонажей\n")
            show_heroes()
            while user_input == 1 or 2:
                team_building(team=user_input)
                user_input = int(input("Желаете добавить ещё игроков? 1-да, 2 - нет "))
                if user_input == 2:
                    print(f"Персонажи первой команды:")
                    team_view(first_team)
                    print(f"Персонажи второй команды:")
                    team_view(second_team)
                    break


def defeated_character(hero):
    """
    Когда умер один из игроков команды, печатается сообщение


    Args:
        hero: список героев одной из команд

    Returns:
    """
    if not hero.current_hp >= 0:
        print(f"Герой {hero.name} мёртв")
        return True
    return False


def main():
    start_game()
    first_team_hero = 0
    second_team_hero = 0

    while True:

        if first_team[first_team_hero].current_hp <= 0:
            print(f'умер {first_team[first_team_hero].name}')
            first_team.remove(first_team[first_team_hero])
            if first_team == []:
                sys.exit("Победила вторая команда")

        elif first_team[first_team_hero].current_hp > 0:
            if check_max_count(first_team_hero, first_team):
                first_team_hero = 0
            if not check_max_count(first_team_hero,first_team):
                first_team_hero += 1

        print("Первая команда нанесла урон:")
        first_team[first_team_hero].hero_damage(second_team[second_team_hero])


        if second_team[second_team_hero].current_hp <= 0:
            second_team.remove(second_team[second_team_hero])
            if second_team == []:
                sys.exit("Победила первая команда")

        elif second_team[second_team_hero].current_hp > 0:
            if check_max_count(second_team_hero, second_team):
                second_team_hero = 0
            if not check_max_count(second_team_hero,second_team):
                second_team_hero += 1

        print("Вторая команда нанесла урон:")
        second_team[second_team_hero].hero_damage(first_team[first_team_hero])



main()
