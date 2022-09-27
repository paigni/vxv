import random

class Hero:
    name = 'name'
    max_hp = 0
    current_hp = max_hp
    damage = 0
    damage_chance = 0

    def hero_damage(self, hero):
        """
        Метод наносит урон игроку противоположенной стороны

        Args:
            hero: Герой из противополежнной стороны
        """
        if random.randint(0,100) <= hero.damage_chance :
            hero.current_hp -= self.damage
        else:
            print("Промах")


class Penguin(Hero):
    name = 'Penguin'
    max_hp = 10
    current_hp = max_hp
    damage = 2
    damage_chance = 90


class Cat(Hero):
    name = 'Cat'
    max_hp = 12
    current_hp = max_hp
    damage = 3
    damage_chance = 70


class Grandma(Hero):
    name = 'Grandma'
    max_hp = 12
    current_hp = max_hp
    damage = 4
    damage_chance = 75


class Teenager(Hero):
    name = 'Teenager'
    max_hp = 20
    current_hp = max_hp
    damage = 1
    damage_chance = 100


class Soldier(Hero):
    name = 'Soldier'
    max_hp = 30
    current_hp = max_hp
    damage = 8
    damage_chance = 80


class StarWarsStormtrooper(Hero):
    name = 'Star Wars Stormtrooper'
    max_hp = 25
    current_hp = max_hp
    damage = 20
    damage_chance = 30


class TrxDinosaur(Hero):
    name = 'Tirex Dinosaur'
    max_hp = 100
    current_hp = max_hp
    damage = 30
    damage_chance = 95