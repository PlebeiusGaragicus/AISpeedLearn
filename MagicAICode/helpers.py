from enum import Enum, auto

# Define the color codes
# BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

class Color(Enum):
    # BLACK = auto()
    RED = auto() # 1
    GREEN = auto()
    YELLOW = auto()
    BLUE = auto()
    MAGENTA = auto()
    CYAN = auto()
    WHITE = auto()

def colored(s: str, color: Color) -> str:
    return f'\033[1;3{color.value}m{s}\033[0m'
