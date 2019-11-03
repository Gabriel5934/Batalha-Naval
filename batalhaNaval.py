# -*- coding: utf-8 -*-

import numpy as np
import time
import sys
from random import randrange

# Definindo variáveis e funções
playerBoard = (np.zeros((8, 8), dtype=str))
playerBoard.fill("■")

harbor = {"porta aviões":"۞", "navio de escolta":"♨", "navio canhoneiro":"☠", "torpedeiro":"☢"}
changeBoat = 0
icons = ["۞", "♨", "☠", "☢"]
found = []

def printBoard():
    for i in range(0, 8):
        print(f"\t\t\t\t\t\t\t\t{playerBoard[i]}")
    print("\n")

def tryAgain():
    print(chr(27) + "[2J")
    print("\t\t\t\t\t\t\t\tAlgo deu errado!")
    time.sleep(0.5)
    print("\t\t\t\t\t\t\t\tTente Novamente!\n")
    printBoard() 

def getPos():
    xAxis = int(input("Digite a cordenada X: "))
    yAxis = int(input("Digite a cordenada Y: "))

def lineRadar():
    yAxis, xAxis = 0, 0
    yAxis += -1
    for i in range(0, 3):
        if botBoard[xAxis + i][yAxis] in icons:
            found.append(botBoard[xAxis + i][yAxis])

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

# Montando o tabuleiro do Cliente
keysList = list(harbor)
for i in range(0, 4):
    try:
        boat = (keysList[changeBoat])
    except:
        print("Isso não deveria acontecer")
    boatSize = len(keysList[changeBoat]) - 8
    if keysList[changeBoat] == "navio canhoneiro":
        boatSize = 6
    if keysList[changeBoat] == "navio de escolta":
        boatSize = 5

    # Definindo posição da embarcação
    validation = False
    while validation == False:
        row = int(input(f"\t\t\t\t\t\t\t\tDigite a linha onde ficará a proa do seu {boat}: "))
        column = int(input(f"\t\t\t\t\t\t\t\tDigite a coluna onde ficará a proa do seu {boat}: "))
        orientation = int(input(f"\t\t\t\t\t\t\t\tPara deixar seu {boat} em pé, digite '1', para deixá-lo deitado, digite '2': "))
        if changeBoat == 0:
            occupiedList = []
        # Validando a posição inserida pelo user
        if row > 8 or column > 8:
            tryAgain()
        elif orientation != 1 and orientation != 2:
            tryAgain()
        elif orientation == 1 and (row - 1) + boatSize > 8:
            tryAgain()
        elif orientation == 2 and (column - 1) + boatSize > 8:
            tryAgain()
        elif orientation == 1:
            for i in range(0, boatSize):
                if [row + i, column] in occupiedList:
                    tryAgain()
                    break
                else:
                    validation = True
        elif orientation == 2:
            for i in range(0, boatSize):
                if [row, column + i] in occupiedList:
                    tryAgain()
                    validation = False
                else:
                    validation = True

    # Colocando as embarcações no tabuleiro
    if orientation == 1:
        for i in range(0, boatSize):
            playerBoard[(row - 1) + i][column - 1] = harbor[boat]
            occupiedList.append([row + i, column])
    if orientation == 2:
        for i in range(0, boatSize):
            playerBoard[row - 1][(column - 1) + i] = harbor[boat]
            occupiedList.append([row, column + i])
    changeBoat += 1

    printBoard()

# Gerando tabuleio do computador
botBoard = (np.zeros((8, 8), dtype=str))
botBoard.fill("■")
changeBoat = 0

keysList = list(harbor)
for i in range(0, 4):
    try:
        boat = (keysList[changeBoat])
    except:
        print("Isso não deveria acontecer")
    boatSize = len(keysList[changeBoat]) - 8
    if keysList[changeBoat] == "navio canhoneiro":
        boatSize = 6
    if keysList[changeBoat] == "navio de escolta":
        boatSize = 5

    # Definindo posição da embarcação
    validation = False
    while validation == False:
        row = randrange(9)
        column = randrange(9)
        orientation = randrange(3)
        if changeBoat == 0:
            occupiedList = []
        # Validando a posição inserida pelo user
        if row > 8 or column > 8:
            validation = False
        elif orientation != 1 and orientation != 2:
            validation = False
        elif orientation == 1 and (row - 1) + boatSize > 8:
            validation = False
        elif orientation == 2 and (column - 1) + boatSize > 8:
            validation = False
        elif row == 0 or column == 0 or orientation == 0:
            validation = False
        elif orientation == 1:
            for i in range(0, boatSize):
                if [row + i, column] in occupiedList:
                    validation = False
                else:
                    validation = True
        elif orientation == 2:
            for i in range(0, boatSize):
                if [row, column + i] in occupiedList:
                    validation = False
                else:
                    validation = True

    # Colocando as embarcações no tabuleiro
    if orientation == 1:
        for i in range(0, boatSize):
            botBoard[(row - 1) + i][column - 1] = harbor[boat]
            occupiedList.append([row + i, column])
    if orientation == 2:
        for i in range(0, boatSize):
            botBoard[row - 1][(column - 1) + i] = harbor[boat]
            occupiedList.append([row, column + i])
    changeBoat += 1

print("Gerando tabuleiro do oponete")
for i in range(0, 10):
    sys.stdout.write("* ")
    sys.stdout.flush()
    time.sleep(0.5)
print("\nGeração concluída!")

print("\n\n For debug purposes")
print(botBoard)
print("\n\n")

# Iniciando o Jogo
print(chr(27) + "[2J")
print('''
 __    __    ______   .______           ___          _______    ______        ______   ______   .___  ___. .______        ___      .___________. _______  __  
|  |  |  |  /  __  \  |   _  \         /   \        |       \  /  __  \      /      | /  __  \  |   \/   | |   _  \      /   \     |           ||   ____||  | 
|  |__|  | |  |  |  | |  |_)  |       /  ^  \       |  .--.  ||  |  |  |    |  ,----'|  |  |  | |  \  /  | |  |_)  |    /  ^  \    `---|  |----`|  |__   |  | 
|   __   | |  |  |  | |      /       /  /_\  \      |  |  |  ||  |  |  |    |  |     |  |  |  | |  |\/|  | |   _  <    /  /_\  \       |  |     |   __|  |  | 
|  |  |  | |  `--'  | |  |\  \----. /  _____  \     |  '--'  ||  `--'  |    |  `----.|  `--'  | |  |  |  | |  |_)  |  /  _____  \      |  |     |  |____ |__| 
|__|  |__|  \______/  | _| `._____|/__/     \__\    |_______/  \______/      \______| \______/  |__|  |__| |______/  /__/     \__\     |__|     |_______|(__) 
                                                                                                                                                                 
''')
arsenal = ["White Head", "Torpedo"]
print('''
\t\t\t\t\t\t\t\tO White Head causa uma explosão em uma área de 3x3 (1 unidade)
\t\t\t\t\t\t\t\tO Tomahawk localiza um barco automaticamente (Obtido ao afundar uma embarcação inimiga)
\t\t\t\t\t\t\t\tO torpedo é suficiente para afundar uma embarcação (Sem restrição de uso)
''')
time.sleep(2)
weapon = int(input(f"Você tem o {arsenal[0]} e o {arsenal[1]} disponível, digite 1 para usar o {arsenal[0]} e 2 para o {arsenal[1]}: "))
xAxis = int(input("Digite a cordenada X do ataque: "))
yAxis = int(input("Digite a cordenada Y do ataque: "))


# Validando as cordenadas
validation = False
while validation == False:
    if xAxis > 8 or xAxis < 0 or yAxis > 8 or xAxis < 0:
        print(chr(27) + "[2J")
        print("\t\t\t\t\t\t\t\tAlgo deu errado!")
        time.sleep(0.5)
        print("\t\t\t\t\t\t\t\tTente Novamente!\n")
        getPos()
        validation = False
    else:
        validation = True

# Iniciando o ataque
if validation == True:
    if weapon == 1:
        xAxis += -2
        for i in range(0, 3):
            lineRadar()
            yAxis += 1
        hittedBoats = len(list(set(found)))
        print(hittedBoats)

                




