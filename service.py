from hero_class import Penguin, Cat, Grandma, Teenager, \
    Soldier, StarWarsStormtrooper, TrxDinosaur

from check import check_hero_choice



def spawn_characters():
    PENGUIN = Penguin()
    CAT = Cat()
    GRANDMA = Grandma()
    TEENAGER = Teenager()
    SOLDIER = Soldier()
    TRXDINOSAUR = TrxDinosaur()
    STARWARSSTORMTROOPER = StarWarsStormtrooper()
    list_of_hero = [PENGUIN, CAT, GRANDMA, TEENAGER, SOLDIER, TRXDINOSAUR, STARWARSSTORMTROOPER]
    return list_of_hero


first_team = []
second_team = []


def team_building(team: int):
    while True:
        user_hero = input("Выберите героя")
        if user_hero.isdigit() and not check_hero_choice(int(user_hero)) :
            hero = spawn_characters()[int(user_hero) - 1]
            user_input = input("Выберите количество")
            if user_input.isdigit():
                count = 0
                while count < int(user_input):
                    count += 1
                    if team == 1:
                        first_team.append(hero)
                    elif team == 2:
                        second_team.append(hero)
                return first_team, second_team
            else:
                print("Количество можно ввести только числом")
        else:
            print("Сейчас можно выбрать героя только от 1 до 7")


def update_count(team,count):
    if len(team) <= count + 1:
        count = 0
    else:
        count += 1

    return count


