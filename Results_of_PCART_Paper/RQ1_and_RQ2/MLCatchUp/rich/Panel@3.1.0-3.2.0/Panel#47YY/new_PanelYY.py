from rich.panel import Panel
from rich.text import Text
from rich.box import ROUNDED
from rich import print
renderable = Text('Hello, World!', justify='center')
panel = Panel(safe_box=None, box=ROUNDED, expand=True, renderable=renderable, style='none', border_style='none')