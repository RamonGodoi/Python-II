from rich.console import Console

console = Console()

def texto_em_negrito(texto, isArquivo=False):
    """
    Mostra o texto em negrito.
    """
    texto = _get_texto(texto, isArquivo)
    console.print(f"[bold]{texto}[/bold]")

def texto_em_italico(texto, isArquivo=False):
    """
    Mostra o texto em itálico.
    """
    texto = _get_texto(texto, isArquivo)
    console.print(f"[italic]{texto}[/italic]")

def _get_texto(texto, isArquivo):
    return open(texto).read() if isArquivo else texto