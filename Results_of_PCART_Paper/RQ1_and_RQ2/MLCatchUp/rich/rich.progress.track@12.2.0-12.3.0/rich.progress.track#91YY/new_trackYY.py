from rich.progress import track
from rich.console import Console
console = Console()
sequence = range(100)
track(sequence, 'Working...', None, True, console, False, None, 10, 'bar.back', 'bar.complete', 'bar.finished', 'bar.pulse', 0.1, show_speed=True)