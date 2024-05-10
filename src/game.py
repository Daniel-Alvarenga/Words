from palavras import *
import random
import os
from unidecode import unidecode
import time

import random
import os
from unidecode import unidecode
import time

cor_letra_correta = ""
cor_letra_deslocada = ""

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def sleep():
    time.sleep(random.randint(200, 250)/1000)
    clear()

quantidade_palavras = len(palavras)

continuar = True

while continuar:
    linhas_1 = []
    linhas_2 = []
    linhas_3 = []

    palavras_inseridas = []
    posicao_palavra = random.randint(0, quantidade_palavras - 1)
    palavra_sorteada = palavras[posicao_palavra]
    palavra_inserida = ""
    tentativas = 7

    length = 5

    clear()

    print("""
        ┌   ┐┌   ┐┌   ┐┌   ┐┌   ┐
          T    E    A    Z    X 
        └   ┘└   ┘└   ┘└   ┘└   ┘
    """)

    sleep()

    print("""
        ┌   ┐\033[38;2;255;165;0m┌───┐\033[0m┌   ┐┌   ┐┌   ┐
          T  \033[38;2;255;165;0m│ W │\033[0m  A    Z    X 
        └   ┘\033[38;2;255;165;0m└───┘\033[0m└   ┘└   ┘└   ┘
    """)
    sleep()


    print("""
        ┌   ┐\033[38;2;255;165;0m┌───┐\033[0m┌   ┐┌   ┐\033[38;2;255;165;0m┌───┐\033[0m
          P  \033[38;2;255;165;0m│ W │\033[0m  A    Z  \033[38;2;255;165;0m│ R │\033[0m
        └   ┘\033[38;2;255;165;0m└───┘\033[0m└   ┘└   ┘\033[38;2;255;165;0m└───┘\033[0m
    """)

    sleep()

    print("""
        ┌   ┐\033[38;2;255;165;0m┌───┐\033[0m┌   ┐┌   ┐\033[38;2;255;165;0m┌───┐\033[0m
          K  \033[38;2;255;165;0m│ W │\033[0m  A    J  \033[38;2;255;165;0m│ R │\033[0m
        └   ┘\033[38;2;255;165;0m└───┘\033[0m└   ┘└   ┘\033[38;2;255;165;0m└───┘\033[0m
    """)

    sleep()

    print("""
        \033[32m╔═══╗\033[0m┌   ┐┌   ┐┌   ┐\033[38;2;255;165;0m┌───┐\033[0m
        \033[32m║ W ║\033[0m  H    A    Y  \033[38;2;255;165;0m│ R │\033[0m
        \033[32m╚═══╝\033[0m└   ┘└   ┘└   ┘\033[38;2;255;165;0m└───┘\033[0m
    """)

    sleep()

    print("""
        \033[32m╔═══╗\033[0m┌   ┐\033[38;2;255;165;0m┌───┐\033[0m┌   ┐\033[38;2;255;165;0m┌───┐\033[0m
        \033[32m║ W ║\033[0m  H  \033[38;2;255;165;0m│ O │\033[0m  Y  \033[38;2;255;165;0m│ R │\033[0m
        \033[32m╚═══╝\033[0m└   ┘\033[38;2;255;165;0m└───┘\033[0m└   ┘\033[38;2;255;165;0m└───┘\033[0m
    """)

    sleep()

    print("""
        \033[32m╔═══╗╔═══╗\033[0m┌   ┐┌   ┐\033[38;2;255;165;0m┌───┐\033[0m
        \033[32m║ W ║║ O ║\033[0m  O    Y  \033[38;2;255;165;0m│ R │\033[0m
        \033[32m╚═══╝╚═══╝\033[0m└   ┘└   ┘\033[38;2;255;165;0m└───┘\033[0m
    """)

    sleep()

    print("""
        \033[32m╔═══╗╔═══╗\033[0m\033[38;2;255;165;0m┌───┐┌───┐┌───┐\033[0m
        \033[32m║ W ║║ O ║\033[0m\033[38;2;255;165;0m│ D ││ S ││ R │\033[0m
        \033[32m╚═══╝╚═══╝\033[0m\033[38;2;255;165;0m└───┘└───┘└───┘\033[0m
    """)

    sleep()

    print("""
        \033[32m╔═══╗╔═══╗\033[0m┌   ┐\033[32m╔═══╗\033[0m\033[38;2;255;165;0m┌───┐\033[0m
        \033[32m║ W ║║ O ║\033[0m  V  \033[32m║ D ║\033[0m\033[38;2;255;165;0m│ R │\033[0m
        \033[32m╚═══╝╚═══╝\033[0m└   ┘\033[32m╚═══╝\033[0m\033[38;2;255;165;0m└───┘\033[0m
    """)

    sleep()

    print("""
        \033[32m╔═══╗╔═══╗\033[0m┌   ┐\033[32m╔═══╗╔═══╗\033[0m
        \033[32m║ W ║║ O ║\033[0m  V  \033[32m║ D ║║ S ║\033[0m
        \033[32m╚═══╝╚═══╝\033[0m└   ┘\033[32m╚═══╝╚═══╝\033[0m
    """)

    sleep()

    print("""
        \033[32m╔═══╗╔═══╗╔═══╗╔═══╗\033[0m┌   ┐
        \033[32m║ W ║║ O ║║ R ║║ D ║\033[0m  F 
        \033[32m╚═══╝╚═══╝╚═══╝╚═══╝\033[0m└   ┘
    """)
    sleep()

    print("""\033[32m
        \033[32m╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗\033[0m
        \033[32m║ W ║║ O ║║ R ║║ D ║║ S ║\033[0m
        \033[32m╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝\033[0m
    """)

    while palavra_inserida != palavra_sorteada:
        tentativa_entrada = 0

        while len(palavra_inserida) != length or not(unidecode(palavra_inserida) in validas_desacentuadas) or palavra_inserida in palavras_inseridas:
            if tentativa_entrada == 1:
                clear()

                print("""\033[32m
        \033[32m╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗\033[0m
        \033[32m║ W ║║ O ║║ R ║║ D ║║ S ║\033[0m
        \033[32m╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝\033[0m
        \033[0m""")
            
            
                for i in range(len(linhas_1)):
                    print(linhas_1[i])
                    print(linhas_2[i])
                    print(linhas_3[i])

                print(f"\n        Word inválida: '{palavra_inserida}'!")
                palavra_inserida = ""
                time.sleep(1.5)

            clear()

            if tentativa_entrada == 2:
                clear()

                print("""\033[32m
        \033[32m╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗\033[0m
        \033[32m║ W ║║ O ║║ R ║║ D ║║ S ║\033[0m
        \033[32m╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝\033[0m
        \033[0m""")
            
            
                for i in range(len(linhas_1)):
                    print(linhas_1[i])
                    print(linhas_2[i])
                    print(linhas_3[i])

                print(f"\n        Word já inserida: '{palavra_inserida}'!")
                palavra_inserida = "" 
                time.sleep(1.5)

            clear()

            print("""\033[32m
        \033[32m╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗\033[0m
        \033[32m║ W ║║ O ║║ R ║║ D ║║ S ║\033[0m
        \033[32m╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝\033[0m
        \033[0m""")
            
            for i in range(len(linhas_1)):
                print(linhas_1[i])
                print(linhas_2[i])
                print(linhas_3[i])

            palavra_inserida = input("\n        Entre com uma word: ").lower()
            tentativa_entrada = 1

            if (unidecode(palavra_inserida) in validas_desacentuadas) and validas[validas_desacentuadas.index(unidecode(palavra_inserida))] in palavras_inseridas:
                tentativa_entrada = 2

        palavra_inserida = validas[validas_desacentuadas.index(unidecode(palavra_inserida))]
        palavras_inseridas.append(palavra_inserida)
        

        linha_1 = "        "
        linha_2 = "        "
        linha_3 = "        "

        situacoes = [0, 0, 0, 0, 0]
        contagem_letras = {}

        for letra in palavra_sorteada:
            contagem_letras[unidecode(letra)] = 0

        for letra in palavra_sorteada:
            contagem_letras[unidecode(letra)] += 1

        for i in range(5):
            if unidecode(palavra_inserida[i]) == unidecode(palavra_sorteada[i]):
                situacoes[i] = 2
                contagem_letras[unidecode(palavra_sorteada[i])] -= 1        

        for i in range(5):
            if unidecode(palavra_inserida[i]) in unidecode(palavra_sorteada) and contagem_letras[unidecode(palavra_inserida[i])] >= 1 and unidecode(palavra_inserida[i]) != unidecode(palavra_sorteada[i]):
                situacoes[i] = 1
                contagem_letras[unidecode(palavra_inserida[i])] -= 1

        for i in range(5):
            if situacoes[i] == 2:
                linha_1 += "\033[32m╔═══╗\033[0m"
                linha_2 += "\033[32m║ "  + palavra_inserida[i].upper() +" ║\033[0m"
                linha_3 += "\033[32m╚═══╝\033[0m"

            elif situacoes[i] == 1:
                linha_1 += "\033[38;2;255;165;0m┌───┐\033[0m"
                linha_2 += "\033[38;2;255;165;0m│ " + palavra_inserida[i].upper() + " │\033[0m"
                linha_3 += "\033[38;2;255;165;0m└───┘\033[0m"

            else:
                linha_1 += "┌   ┐"
                linha_2 += "  " + palavra_inserida[i].upper() + "  "
                linha_3 += "└   ┘"

        linhas_1.append(linha_1)
        linhas_2.append(linha_2)
        linhas_3.append(linha_3)

        clear()

        print("""\033[32m
        \033[32m╔═══╗╔═══╗╔═══╗╔═══╗╔═══╗\033[0m
        \033[32m║ W ║║ O ║║ R ║║ D ║║ S ║\033[0m
        \033[32m╚═══╝╚═══╝╚═══╝╚═══╝╚═══╝\033[0m
        """)
        
        for i in range(len(linhas_1)):
            print(linhas_1[i])
            print(linhas_2[i])
            print(linhas_3[i])

        if (unidecode(palavra_inserida) == unidecode(palavra_sorteada)):
            print("\n      Parabéns, você acertou!")
            break
        else:
            tentativas -= 1
            if tentativas == 0:
              print("\n      Que pena, você perdeu...")
              print(f"      A word secreta era: {palavra_sorteada.upper()}.")
              break

            palavra_inserida = ""
    
    continuar = input("\n      1 jogar - 0 sair: ") == '1'

print("\n      Obrigado por jogar WORDS!")
print("      Daniel R. Alvarenga - 05/2024\n")