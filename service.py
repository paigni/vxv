from hero_class import Penguin, Cat, Grandma, Teenager, \
    Soldier, StarWarsStormtrooper, TrxDinosaur



PENGUIN = Penguin()
CAT = Cat()
GRANDMA = Grandma()
TEENAGER = Teenager()
SOLDIER = Soldier()
TRXDINOSAUR = TrxDinosaur()
STARWARSSTORMTROOPER = StarWarsStormtrooper()

list_of_hero = [PENGUIN, CAT, GRANDMA, TEENAGER, SOLDIER, TRXDINOSAUR, STARWARSSTORMTROOPER]
first_team = []
second_team = []



def available_heroes():
    """
        Выводит список героев доступных на текущий момент
    """
    print("Вам доступны следующие герои:\n")
    count = 0
    for hero in list_of_hero:
        count += 1
        print(f"{count}){hero.name}: здоровье {hero.max_hp} \n"
              f"урон {hero.damage}, и шанс попадания {hero.damage_chance}")




