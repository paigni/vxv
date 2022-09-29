import sys
import time

from service import spawn_characters, team_building, first_team, second_team
from check import check_choice, check_hero_hp
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

    user_input = input(f'Добро пожаловать в игру, чтобы начать нажмите 1\n'
                           f'для того чтобы выйти нажмите 2\n')
    if int(user_input) == 1:
        use_input = int(input("Выберите сторону для выбора персонажей \n 1-Силы света \n 2-Силы тьмы\n"))
        if use_input == 1:
            print("Выбор персонажей первой команды\n")
            while user_input != 2:
                show_heroes()
                team_building(team=1)
                user_input = int(input("Желаете добавить ещё игроков? 1-да, 2 - нет "))
                if user_input == 2:
                    print("Выбор персонажей второй команды\n")
                    team_building(team=2)
                    user_input = int(input("Желаете добавить ещё игроков? 1-да, 2 - нет "))
                    if user_input == 2:
                        print(f"Персонажи первой команды:")
                        team_view(first_team)
                        print(f"Персонажи второй команды:")
                        team_view(second_team)
                        break
        elif use_input == 2:
            print("Выбор персонажей второй команды\n")
            show_heroes()
            while user_input != 2:
                team_building(team=2)
                user_input = int(input("Желаете добавить ещё игроков? 1-да, 2 - нет "))
                if user_input == 2:
                    print("Выбор персонажей первой команды\n")
                    show_heroes()
                    user_input = 1
                    while user_input != 2:
                        team_building(team=1)
                        user_input = int(input("Желаете добавить ещё игроков? 1-да, 2 - нет "))
                        if user_input == 2:
                            print(f"Персонажи первой команды:")
                            team_view(first_team)
                            print(f"Персонажи второй команды:")
                            team_view(second_team)
                            break
        else:
            print('Неверный ввод,пожалуйста введите значение 1 или 2')



def defeated_character(hero_list: list):
    """
    Когда умер один из игроков команды, печатается сообщение


    Args:
        hero_list: список героев одной из команд

    Returns:
    """
    for hero in hero_list:
        if not check_hero_hp(hero):
            hero_list.remove(hero)
            print(f"Герой {hero.name} мёртв")
    return hero_list


def main():
    start_game()
    first_team_hero = 0
    second_team_hero = 0
    while not first_team or second_team:
        print("Первая команда нанесла урон:")
        first_team[first_team_hero].hero_damage(second_team[0])
        defeated_character(second_team)
        print("Вторая команда нанесла урон:")
        second_team[second_team_hero].hero_damage(first_team[0])
        defeated_character(first_team)
        if not first_team:
            print("Победила вторая команда")
            break
        elif not second_team:
            print("Победила первая команда")
            break



main()