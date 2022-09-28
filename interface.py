import sys
import time

from service import create_list,team_building,first_team,second_team
from check import  check_choice
from collections import Counter


def available_heroes():
    """
        Выводит список героев доступных на текущий момент
    """
    print("Вам доступны следующие герои:\n")
    count = 0
    for hero in create_list():
        count += 1
        print(f"{count}){hero.name}: здоровье {hero.max_hp} \n"
              f"урон {hero.damage}, и шанс попадания {hero.damage_chance}")


def team_view(team:list):
    team = Counter(team)
    for key,value in team.items():
        print(f"{key.name}-{value}")


def start_game():
    """
    Функция начала игры

    Returns:
        Ввод пользователя
    """

    user_input = 4
    while not check_choice(user_input):
        user_input = input(f'Добро пожаловать в игру, чтобы начать нажмите 1\n'
                           f'для того чтобы выйти нажмите 2\n')
        if int(user_input) == 1:
            user_input = input("Выберите сторону для выбора персонажей \n 1-Силы света \n 2-Силы тьмы\n")
            if user_input == '1':
                print("Выбор персонажей сил света\n")
                available_heroes()
                while user_input !=2:
                    team_building(1)
                    user_input = input("Желаете добавить ещё игроков? 1-да, 2 - нет ")
                print("Выбор персонажей сил тьмы\n")
                available_heroes()
                while user_input != 2:
                    team_building(2)
                    user_input = input("Желаете добавить ещё игроков? 1-да, 2 - нет ")
            if user_input == '2':
                print("Выбор персонажей сил тьмы\n")
                available_heroes()
                team_building(2)
                print("Выбор персонажей сил света\n")
                available_heroes()
                team_building(1)
            print(f"Персонажи сил света:\n{team_view(first_team)}")
            print(f"Персонажи сил тьмы:\n{team_view(second_team)}")
            user_input = input("Вы закончили выбор? Начинаем игру? \n 1-нет \n 2-да")
            if user_input == '2':
                break
        else:
            print('Неверный ввод,пожалуйста введите значение 1 или 2')


start_game()
