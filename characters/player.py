from character import *

class Player(Character):
    def __init__(self, name, hp, str, money, int):
        Character.__init__(self, name, hp, money)
        self.str = str
        self.int = int