# coding: utf-8
# license: GPLv3
from gameunit import *

#FIXME:
"""В этом файле должен быть описан класс героя, унаследованный от Attacker
Герой должен иметь 100 поинтов здоровья, атаку 50, опыт 0, имя, задаваемое в конструкторе
Метод attack должен получать атрибут target и уменьшать его здоровье на величину атаки.

"""
class Hero(Attacker):
    def __init__(self,name):
        self.name=None
        self._health = 100
        self._attack = 50
        self._experience = 0
    def attack(self,target):
        target._health -= self._attack
        self._experience+=10
    def gameOver(self):
        if _health==0:
            print("Game Over, Little Boy.Experience earned:",hero._experience)




