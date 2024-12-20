from aventura_pkg.labirinto import criar_labirinto, imprimir_labirinto
from aventura_pkg.jogador import iniciar_jogador, mover
from aventura_pkg.utils import imprime_instrucoes, imprime_menu

def main():
    nome = input("Digite seu nome: ")
    imprime_menu(nome)

    while True:
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            dificuldade = int(input("Escolha a dificuldade (1-3): "))
            labirinto = criar_labirinto(dificuldade)
            jogador = iniciar_jogador(labirinto)
            imprimir_labirinto(labirinto)
            
            while True:
                comando = mover(jogador, labirinto)
                imprimir_labirinto(labirinto)
                if comando == "sair" or labirinto[-1][-1] == "P":
                    break
            
        elif opcao == "2":
            imprime_instrucoes()
        elif opcao == "3":
            print("Até mais!")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
