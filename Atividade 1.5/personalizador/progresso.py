from rich.progress import Progress
from time import sleep

def barra_progresso_simples(texto, isArquivo=False):
    """
    Mostra uma barra de progresso simples.
    """
    texto = _get_texto(texto, isArquivo)
    with Progress() as progress:
        task = progress.add_task("[green]Carregando...", total=100)
        for _ in range(100):
            sleep(0.02)
            progress.update(task, advance=1)

def progresso_com_mensagem(texto, isArquivo=False):
    """
    Mostra uma barra de progresso com mensagem.
    """
    texto = _get_texto(texto, isArquivo)
    with Progress() as progress:
        task = progress.add_task(f"[cyan]{texto}...", total=100)
        for _ in range(100):
            sleep(0.02)
            progress.update(task, advance=1)

def _get_texto(texto, isArquivo):
    return open(texto).read() if isArquivo else texto