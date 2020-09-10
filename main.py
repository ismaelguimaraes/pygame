# Arquivo principal do jogo
from characters.player import *

player = Player("Padrão", 1, 1, 1, 1)

def main():
    name = input("Insira o nome do seu personagem:")
    player.name = name
    print ("Seu nome é ", name)

main()