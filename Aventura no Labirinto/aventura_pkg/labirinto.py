import random

def criar_labirinto(dificuldade):
    tamanho = {1: 5, 2: 7, 3: 10}[dificuldade]
    labirinto = [[random.choice([" ", "#", "@"]) for _ in range(tamanho)] for _ in range(tamanho)]
    labirinto[0][0] = "P"  # Posição inicial do jogador
    labirinto[-1][-1] = "S"  # Saída do labirinto
    return labirinto

def imprimir_labirinto(labirinto):
    for linha in labirinto:
        print("".join(linha))
