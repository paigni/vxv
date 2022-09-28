from hero_class import Penguin, Cat, Grandma, Teenager, \
    Soldier, StarWarsStormtrooper, TrxDinosaur

from check import check_hero_choice,check_choice


def create_list():
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
    if not check_choice('5'):
        print("Выберите героя")
        user_hero = int(input())
        if not check_hero_choice(user_hero):
            hero = create_list()[user_hero - 1]
            user_input = input("Выберите количество")
            count = 0
            while count <= int(user_input):
                count += 1
                if team == 1:
                    first_team.append(hero)
                elif team == 2:
                    second_team.append(hero)
        return first_team,second_team

