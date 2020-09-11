# Main game file

from characters.player import *
from commands import *
from utilities.util import *

def help(player, args):
    for command in commands:
        print(command)

commands = {
    'help': help,
    'exit': exit
}

invisible = {
    'quit': exit,
    'water': help
}

player = Player("Ismael Lindo", 1, 1, 1)

def nameInput(prompt):
    name = input(prompt)
    return name.strip()

def getName():
    tempName = ""
    while 1:
        tempName = nameInput("What is your name? ")

        if len(tempName) < 1:
            continue

        yes = yesOrNo(tempName + ", is that your name? (Y/N): ")

        if yes:
            return tempName
        else:
            continue

def isValidCMD(cmd):
    if cmd in commands:
        return True
    elif cmd in invisible:
        return True
    return False

def runCMD(cmd, args, player):
    commands[cmd](player, args)

def main(player):
    
    player.name = getName()

    while (not player.dead):
        line = input(">> ")
        words = line.split()
        words.append("EOI")

        if isValidCMD(words[0]):
            runCMD(words[0], words[1], player)

main(player)