# Main game file

from characters.player import *

commands = {
    'help': help,
    'exit': exit
}

player = Player("Default", 1, 1, 1)

def isValidCMD(cmd):
    if cmd in commands:
        return True
    return False


def main(player):

    while (not player.dead):
        line = input(">> ")
        Input = line.split()

        if isValidCMD(Input[0]):
            print(Input[0])


        print(Input)

main(player)