# Абстрактный класс для оружия
from abc import ABC, abstractmethod


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass


# Класс для меча
class Sword(Weapon):
    def attack(self):
        return "удар мечом"


# Класс для лука
class Bow(Weapon):
    def attack(self):
        return "выстрел из лука"


# Класс Истребитель
class Fighter:
    def __init__(self, name):
        self.name = name
        self.weapon = None

    def changeWeapon(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon:
            print(f'{self.name} делает {self.weapon.attack()}.')
        else:
            print(f'{self.name} безоружен и не может атаковать.')


# Реализация боя
class Monster:
    def __init__(self, name):
        self.name = name
        self.is_defeated = False

    def defeat(self):
        self.is_defeated = True
        print(f'{self.name} побежден!')


def battle(fght, mnst):
    fght.attack()
    mnst.defeat()


# Создаем бойца и монстра
fighter = Fighter("Боец")
monster = Monster("Монстр")

# Боец выбирает меч
sword = Sword()
fighter.changeWeapon(sword)
battle(fighter, monster)

# Боец выбирает лук
bow = Bow()
fighter.changeWeapon(bow)
battle(fighter, monster)
