class Character(object):
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp
        
        self.dead = False

    def attack(self, other):
        pass

    def update(self):
        if self.hp <= 0:
            self.dead = True
            self.hp = 0