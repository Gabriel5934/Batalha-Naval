# -*- coding: utf-8 -*-

import numpy as np
import time
import sys
from random import randrange

# Definindo variáveis e funções
playerBoard = (np.zeros((8, 8), dtype=str))
playerBoard.fill("■")

arsenal = {"porta aviões":"۞", "navio de escolta":"♨", "navio canhoneiro":"☠", "torpedeiro":"☢"}
changeBoat = 0

def printBoard():
    for i in range(0, 8):
        print(f"\t\t\t\t\t\t\t\t{playerBoard[i]}")
    print("\n")

def tryAgain():
    print(chr(27) + "[2J")
    print("\t\t\t\t\t\t\t\tAlgo deu errado!")
    time.sleep(1)
    print("\t\t\t\t\t\t\t\tTente Novamente!\n")
    printBoard() 

# Tela inicial
print('''
.______        ___      .___________.     ___       __       __    __       ___         .__   __.      ___      ____    ____      ___       __      
|   _  \      /   \     |           |    /   \     |  |     |  |  |  |     /   \        |  \ |  |     /   \     \   \  /   /     /   \     |  |     
|  |_)  |    /  ^  \    `---|  |----`   /  ^  \    |  |     |  |__|  |    /  ^  \       |   \|  |    /  ^  \     \   \/   /     /  ^  \    |  |     
|   _  <    /  /_\  \       |  |       /  /_\  \   |  |     |   __   |   /  /_\  \      |  . `  |   /  /_\  \     \      /     /  /_\  \   |  |     
|  |_)  |  /  _____  \      |  |      /  _____  \  |  `----.|  |  |  |  /  _____  \     |  |\   |  /  _____  \     \    /     /  _____  \  |  `----.
|______/  /__/     \__\     |__|     /__/     \__\ |_______||__|  |__| /__/     \__\    |__| \__| /__/     \__\     \__/     /__/     \__\ |_______|
                                                                                                                                                    
''')
print("\t\t\t\t\t\t\t\tCarregando\n")
for i in range(0, 150):
    sys.stdout.write("█")        
    sys.stdout.flush()
    time.sleep(0.005)
time.sleep(1)
print(chr(27) + "[2J")
printBoard()

# Iniciando o jogo
keysList = list(arsenal)
for i in range(0, 4):
    try:
        boat = (keysList[changeBoat])
    except:
        print("Isso não deveria acontecer")

    # Definindo posição da embarcação
    validation = False
    while validation == False:
        row = int(input(f"\t\t\t\t\t\t\t\tDigite a linha onde ficará a proa do seu {boat}: "))
        column = int(input(f"\t\t\t\t\t\t\t\tDigite a coluna onde ficará a proa do seu {boat}: "))
        orientation = int(input(f"\t\t\t\t\t\t\t\tPara deixar seu {boat} em pé, digite '1', para deixá-lo deitado, digite '2': "))

        # Validando a posição inserida pelo user
        if row > 8 or column > 8:
            tryAgain()
        elif orientation != 1 and orientation != 2:
            tryAgain()
        elif playerBoard[row - 1][column - 1] == arsenal[boat]:
            tryAgain()
        elif orientation == 1 and (column - 1) + 4 > 8:
            tryAgain()
        elif orientation == 2 and (row - 1) + 4 > 8:
            tryAgain()
        else:
            validation = True

    # Colocando as embarcações no tabuleiro
    if orientation == 1:
        for i in range(0, 4):
            playerBoard[(row - 1) + i][column - 1] = arsenal[boat]
    if orientation == 2:
        for i in range(0, 4):
            playerBoard[row - 1][(column - 1) + i] = arsenal[boat]
    changeBoat += 1

    printBoard()

print("Gerando tabuleiro do oponete")
for i in range(0, 10):
    sys.stdout.write("* ")
    sys.stdout.flush()
    time.sleep(0.5)
print("\nGeração concluída!")








