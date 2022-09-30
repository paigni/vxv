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

    use_input = input(f'Добро пожаловать в игру, чтобы начать нажмите 1\n'
                      f'для того чтобы выйти нажмите 2\n')
    if use_input == '1' and use_input.isdigit():
        user_input = 4
        while user_input == 1 or 2:
            user_input = int(input("Выберите сторону для выбора персонажей \n "
                                   "1-Первая команда \n 2-Вторая команда\n 3-Начать игру\n"))
            if user_input == 3:
                if first_team == [] or second_team == []:
                    print("Для начала игры нужно добавить героев в обе команды")
                    user_input = 1
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
                    else:
                        continue
    else:
        print("Неверный ввод,введите 1 или 2")
        while use_input == '1' and use_input.isdigit():
            use_input = input()



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
    copy_first_team = first_team.copy()
    copy_second_team = second_team.copy()
    while first_team or second_team:
        if not first_team:
            sys.exit("Победила вторая команда")

        if not second_team:
            sys.exit("Победила первая команда")

        if not copy_first_team and first_team != []:
            copy_first_team = first_team.copy()
            continue

        if not copy_second_team and second_team != []:
            copy_second_team = second_team.copy()
            continue



        copy_first_team[0].hero_damage(second_team[0])
        if not defeated_character(second_team[0]):
            print("Вторая команда нанесла урон:")
            copy_second_team[0].hero_damage(first_team[0])
            copy_second_team.pop(0)

            if not defeated_character(first_team[0]):
                copy_first_team.pop(0)
                time.sleep(0.1)
                continue

            if defeated_character(first_team[0]) and first_team != []:
                first_team.pop(0)
                copy_first_team = first_team.copy()
                time.sleep(0.1)
                continue


        elif defeated_character(second_team[0]) and second_team != []:
            second_team.pop(0)

            if second_team == []:
                sys.exit("Победила первая команда")

            if first_team == []:
                sys.exit("Победила вторая команда")

            copy_second_team = second_team.copy()
            print("Вторая команда нанесла урон:")
            copy_second_team[0].hero_damage(first_team[0])

            if not defeated_character(first_team[0]):
                copy_first_team.pop(0)
                time.sleep(0.1)
                continue

            elif defeated_character(first_team[0]) and first_team != []:
                first_team.pop(0)
                copy_first_team = first_team.copy()
                time.sleep(0.1)
                continue



main()
