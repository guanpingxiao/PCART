from rich.console import Console
from rich.theme import Theme
from rich.highlighter import ReprHighlighter
from datetime import datetime
import sys
console = Console(get_datetime=datetime.now, soft_wrap=False, stderr=False, style=None)