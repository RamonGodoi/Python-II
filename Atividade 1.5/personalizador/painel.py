from rich.panel import Panel
from rich.console import Console

console = Console()

def painel_simples(texto, isArquivo=False):
    """
    Mostra o texto em um painel simples.
    """
    texto = _get_texto(texto, isArquivo)
    panel = Panel(texto, title="Painel Simples", border_style="blue")
    console.print(panel)

def painel_com_titulo(texto, isArquivo=False):
    """
    Mostra o texto em um painel com título e bordas coloridas.
    """
    texto = _get_texto(texto, isArquivo)
    panel = Panel(texto, title="Painel com Título", border_style="green")
    console.print(panel)

def _get_texto(texto, isArquivo):
    return open(texto).read() if isArquivo else texto