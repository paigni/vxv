import sys
import time

from service import spawn_characters, team_building, first_team, second_team
from collections import Counter


def show_heroes():
    """
        Выводит список героев доступных на текущий момент
    """
    print("Вам доступны следующие герои:\n")
    count = 0
    for hero in spawn_characters():
        time.sleep(0.2)
        count += 1
        print(f"{count}){hero.name}: здоровье {hero.max_hp} \n"
              f"урон {hero.damage}, и шанс попадания {hero.damage_chance}")


def team_view(team: list):
    """
    Выводит текущих игроков одной из команд
    Args:
        team: список команды
    """
    team = Counter(team)
    for key, value in team.items():
        print(f"{key.name}-{value}")


def start_game():
    """
    Функция начала игры,

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
        user_input = input("Выберите сторону для выбора персонажей \n "
                            "1-Первая команда \n 2-Вторая команда\n 3-Начать игру\n")
        if user_input.isdigit():
            if int(user_input) == 3:
                if first_team == [] or second_team == []:
                    print("Для начала игры нужно добавить героев в обе команды")
                    continue
                else:
                    print("Игра началась")
                    break
            elif int(user_input) == 1 or int(user_input) == 2:
                show_heroes()
                team_building(team=int(user_input))

                while True:
                    user_choice = input("Желаете добавить ещё игроков? 1-да, 2 - нет ")

                    if user_choice.isdigit() and int(user_choice) == 2:
                        print(f"Персонажи первой команды:")
                        team_view(first_team)
                        print(f"Персонажи второй команды:")
                        team_view(second_team)
                        break

                    elif user_choice.isdigit() and int(user_choice) == 1:
                        team_building(team=int(user_input))
                        continue

                    else:
                        print("Должно быть число 1 или 2")
        else:
            print("Ввод должен быть числом 1,2 или 3")