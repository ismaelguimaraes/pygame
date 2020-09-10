from character import *

class Enemy(Character):
    def __init__(self, name, hp, money, str):
        Character.__init__(self, name, hp, money)
        self.str = str