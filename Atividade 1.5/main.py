import argparse
from personalizador import layout, painel, progresso, estilo

MODULOS = {
    "layout": layout,
    "painel": painel,
    "progresso": progresso,
    "estilo": estilo
}

FUNCOES = {
    "layout": ["layout_simples", "layout_complexo"],
    "painel": ["painel_simples", "painel_com_titulo"],
    "progresso": ["barra_progresso_simples", "progresso_com_mensagem"],
    "estilo": ["texto_em_negrito", "texto_em_italico"]
}

def main():
    parser = argparse.ArgumentParser(description="Personalizador de texto com Rich.")
    parser.add_argument("texto", help="Texto ou caminho do arquivo.")
    parser.add_argument("-a", "--arquivo", action="store_true", help="Indica que o argumento é um arquivo.")
    parser.add_argument("-m", "--modulo", choices=MODULOS.keys(), required=True, help="Módulo a ser usado.")
    parser.add_argument("-f", "--funcao", required=True, help="Função do módulo a ser chamada.")
    args = parser.parse_args()

    modulo = MODULOS[args.modulo]
    if args.funcao in FUNCOES[args.modulo]:
        funcao = getattr(modulo, args.funcao)
        funcao(args.texto, args.arquivo)
    else:
        print(f"Função inválida. Escolha entre: {', '.join(FUNCOES[args.modulo])}")

if __name__ == "__main__":
    main()
