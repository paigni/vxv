import sys
import time

from service import available_heroes, first_team, second_team, list_of_hero
from check import check_hero_choice, check_choice


def team_building(team: int):
    if team == 1:
        print("Выберите героев первой команды")
    elif team == 2:
        print("Выберите героев второй команды")
    user_input = 'd'
    while not user_input.isdigit():
        user_input = input()
        if check_hero_choice(user_input):
            hc = int(user_input)
            hero = list_of_hero[hc - 1]
            print(hero)
            user_input = 'd'
            while not user_input.isdigit:
                user_input = input("Выберите количество")
                count = 0
                while count <= int(user_input):
                    count += 1
                    if team == 1:
                        first_team.append(hero)
                    elif team == 2:
                        second_team.append(hero)



def poctor(c):
        team_building(c)
        user_input = 'd'
        while not user_input.isdigit():
            hc_input = input("Желаете добавить ещё игроков? 1-да, 2 - нет ")
            if hc_input.isdigit() and check_choice(hc_input):
                hc_input = int(hc_input)
                if hc_input == 1:
                    team_building(c)
                else:
                    break
            else:
                print("Неверный ввод,повторите попытку")


def start_game():
    """
    Функция начала игры

    Returns:
        Ввод пользователя
    """

    print(f'Добро пожаловать в игру, чтобы начать нажмите 1\n'
          f'для того чтобы выйти нажмите 2')
    user_input = 'd'
    while not user_input.isdigit():
        user_input = input()
        if user_input.isdigit() and check_choice(user_input):
            if int(user_input) == 1:
                available_heroes()
                poctor(1)
                poctor(2)
                print(first_team,second_team)
        else:
            print('Неверный ввод,пожалуйста введите значение 1 или 2')


start_game()
