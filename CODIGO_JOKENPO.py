import random
import os
import time
pontos_player1 = 0
pontos_player2 = 0
pontos_player = 0
pontos_computador = 0
player1 = 0
player2 = 0

os.system("cls")
print("JO-KEN-PÔ!\n")
# Selecionar modo de jogo:
modo = int(input("Escolha um modo de jogo:\n1. Jogador VS Jogador\n2. Jogador VS Computador\n0. Sair\n"))

# ------------------- NO JOGO -------------------
while modo != 0:

    if modo == 1:
        
        pontos_computador = 0
        pontos_player = 0

        print("\n          Modo JOGADOR VS JOGADOR Selecionado\n")
        print(f"----- JOGADOR 1: {pontos_player1} pontos   JOGADOR 2: {pontos_player2} pontos -----\n")

        player1 = int(input("JOGADOR 1 - Digite 1 para PEDRA, 2 para PAPEL, ou 3 para TESOURA:\n"))
        os.system("cls")
        player2 = int(input("JOGADOR 2 - Digite 1 para PEDRA, 2 para PAPEL, ou 3 para TESOURA:\n"))

    # ------------------- VS Computador ---------------
    if modo == 2:
        
        pontos_player1 = 0
        pontos_player2 = 0

        print("         Modo VS COMPUTADOR Selecionado\n")
        print(f"----- VOCÊ: {pontos_player} pontos  COMPUTADOR: {pontos_computador} pontos -----\n")
        
        player1 = int(input("JOGADOR - Digite 1 para PEDRA, 2 para PAPEL, ou 3 para TESOURA:\n"))
        # Escolha do Computador:
        player2 = random.randint(1, 3)
        
        print("Hora do computador escolher. . .    1.PEDRA 2.PAPEL 3.TESOURA")
        time.sleep(2)
        print(f"O computador escolheu {player2}!")
        time.sleep(2)

    
    # PLAYER 1 PERDE:
    if (player1 == 1 and player2 == 2) or (player1 == 2 and player2 == 3) or (
            player1 == 3 and player2 == 1):

        if modo == 1:
            print("\nJOGADOR 2 GANHOU!\n")
            pontos_player2 += 1
            print(f"----- JOGADOR 1: {pontos_player1} pontos   JOGADOR 2: {pontos_player2} pontos -----\n")
        if modo == 2:
            print("\nCOMPUTADOR GANHOU!\n")
            pontos_computador += 1
            print(f"----- JOGADOR 1: {pontos_player} pontos   COMPUTADOR: {pontos_computador} pontos -----\n")

    # PLAYER 1 GANHA:
    elif (player1 == 2 and player2 == 1) or (player1 == 3 and player2 == 2) \
            or (player1 == 1 and player2 == 3):

        print("\nJOGADOR 1 GANHOU!\n")
        if modo == 1:
            pontos_player1 += 1
            print(f"----- JOGADOR 1: {pontos_player1} pontos   JOGADOR 2: {pontos_player2} pontos -----\n")
        if modo == 2:
            pontos_player += 1
            print(f"----- JOGADOR 1: {pontos_player} pontos   COMPUTADOR: {pontos_computador} pontos -----\n")

    # EMPATE:
    elif (player1 == 1 and player2 == 1) or (player1 == 2 and player2 == 2) \
            or (player1 == 3 and player2 == 3):
        
        print("\nEMPATE\n")
        if modo == 1:
            print(f"----- JOGADOR 1: {pontos_player1} pontos   JOGADOR 2: {pontos_player2} pontos -----\n")
        if modo == 2:
            print(f"----- JOGADOR 1: {pontos_player} pontos   COMPUTADOR: {pontos_computador} pontos -----\n")

    # JOGADA INVÁLIDA:
    else:
        print("\nJogo inválido! certifique-se se digitou uma opção válida")
        if modo == 1:
            print(f"----- JOGADOR 1: {pontos_player1} pontos   JOGADOR 2: {pontos_player2} pontos -----\n")
        if modo == 2:
            print(f"----- JOGADOR 1: {pontos_player} pontos   COMPUTADOR: {pontos_computador} pontos -----\n")
    if modo > 2:
        print("\ninválido! certifique-se se digitou uma opção válida")

    modo = int(input("Selecione uma opção:\n1. Humano VS Humano \n""2. Computador VS Computador \n0. Sair\n"))

print("Obrigado por jogar!!!!\n")
