# Main game file

from characters.player import *

player = Player("Default", 1, 1, 1)

def main():
    name = input("What is your name? ")
    player.name = name
    print("Your name is ", player.name)

main()