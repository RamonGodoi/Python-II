from rich.console import Console

console = Console()

def imprime_instrucoes():
    console.print("[bold blue]Bem-vindo à Aventura no Labirinto![/bold blue]")
    console.print("[green]Use as setas do teclado para mover o personagem.[/green]")
    console.print("[red]Colete itens e encontre a saída para vencer![/red]")

def imprime_menu(nome):
    console.print(f"[bold yellow]Olá {nome}, bem-vindo ao jogo![/bold yellow]")
    console.print("Escolha uma opção:")
    console.print("1. Jogar")
    console.print("2. Instruções")
    console.print("3. Sair")
