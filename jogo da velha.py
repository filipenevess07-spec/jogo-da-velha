import random

JOGADOR = "X"
COMPUTADOR = "O"
def criar_tabuleiro():
    return [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]

def imprimir_tabuleiro(tabuleiro):
    print()
    for i in range(3):
        print(tabuleiro[i][0] + " | " + tabuleiro[i][1] + " | " + tabuleiro[i][2])
        if i < 2:
            print("---------")

def verificar_vitoria(tabuleiro, simbolo):
    # linhas
    for i in range(3):
        if tabuleiro[i][0] == simbolo and tabuleiro[i][1] == simbolo and tabuleiro[i][2] == simbolo:
            return True

    # colunas
    for j in range(3):
        if tabuleiro[0][j] == simbolo and tabuleiro[1][j] == simbolo and tabuleiro[2][j] == simbolo:
            return True

    # primeira diagonal
    if tabuleiro[0][0] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][2] == simbolo:
        return True

    # segunda diagonal
    if tabuleiro[0][2] == simbolo and tabuleiro[1][1] == simbolo and tabuleiro[2][0] == simbolo:
        return True

    return False
def ler_numero(mensagem):
   # ler a jogada do usuario
    # restrição para valores foras do tabuleiro
    while True:
        valor = int(input(mensagem))
        if valor == 0 or valor == 1 or valor == 2:
            return valor
        else:
            print("Valor inválido! Digite apenas 0, 1 ou 2.")

def ler_posicao(tabuleiro):
    while True:
        linha = ler_numero("Digite a linha (0, 1 ou 2): ")
        coluna = ler_numero("Digite a coluna (0, 1 ou 2): ")

        if tabuleiro[linha][coluna] == " ":
            return linha, coluna

        print("Posição já utilizada! Escolha outra.")

def jogada_computador(tabuleiro):
    linha_pc = random.randint(0, 2)
    coluna_pc = random.randint(0, 2)

    while tabuleiro[linha_pc][coluna_pc] != " ":
        linha_pc = random.randint(0, 2)
        coluna_pc = random.randint(0, 2)

    return linha_pc, coluna_pc

tabuleiro = criar_tabuleiro()
jogadas = 0
ganhou = False

while jogadas < 9 and ganhou == False:

    imprimir_tabuleiro(tabuleiro)

    print("Sua vez (" + JOGADOR + ")")
    print ()
    linha, coluna = ler_posicao(tabuleiro)

    tabuleiro[linha][coluna] = JOGADOR
    jogadas += 1
    print ()
    ganhou = verificar_vitoria(tabuleiro, JOGADOR)

    if ganhou == True:
        print("======VOCÊ GANHOU!======")
    else:
        if jogadas < 9:
            linha_pc, coluna_pc = jogada_computador(tabuleiro)
            tabuleiro[linha_pc][coluna_pc] = COMPUTADOR
            jogadas += 1

            print("Computador jogou em:", linha_pc, coluna_pc)

            ganhou = verificar_vitoria(tabuleiro, COMPUTADOR)

            if ganhou == True:
                print("======COMPUTADOR GANHOU!======")
imprimir_tabuleiro(tabuleiro)
if ganhou == False:
    print("VELHA!")