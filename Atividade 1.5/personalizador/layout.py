from rich.console import Console
from rich.layout import Layout

console = Console()

def layout_simples(texto, isArquivo=False):
    """
    Mostra o texto em um layout simples.
    """
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="body", ratio=1)
    )
    layout["header"].update("[bold magenta]Cabeçalho")
    layout["body"].update(_get_texto(texto, isArquivo))
    console.print(layout)

def layout_complexo(texto, isArquivo=False):
    """
    Mostra o texto em um layout mais detalhado.
    """
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="footer", size=3),
        Layout(name="body", ratio=1)
    )
    layout["header"].update("[bold green]Topo do Layout")
    layout["footer"].update("[bold blue]Rodapé")
    layout["body"].update(_get_texto(texto, isArquivo))
    console.print(layout)

def _get_texto(texto, isArquivo):
    return open(texto).read() if isArquivo else texto