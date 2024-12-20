def iniciar_jogador(labirinto):
    labirinto[0][0] = "P"
    return {"posicao": (0, 0), "pontuacao": 0}

def mover(jogador, labirinto):
    x, y = jogador["posicao"]
    comando = input("Digite um comando (w/a/s/d): ")
    nova_posicao = (x, y)

    if comando == "w" and x > 0:
        nova_posicao = (x - 1, y)
    elif comando == "s" and x < len(labirinto) - 1:
        nova_posicao = (x + 1, y)
    elif comando == "a" and y > 0:
        nova_posicao = (x, y - 1)
    elif comando == "d" and y < len(labirinto[0]) - 1:
        nova_posicao = (x, y + 1)
    elif comando == "sair":
        return "sair"

    if labirinto[nova_posicao[0]][nova_posicao[1]] != "#":
        labirinto[x][y] = " "
        x, y = nova_posicao
        jogador["posicao"] = (x, y)
        labirinto[x][y] = "P"

    return comando
