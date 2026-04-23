COLORS = {
    "red": "\033[31m",
    "green": "\033[32m",
    "blue": "\033[34m",
    "yellow": "\033[33m",
    "cyan": "\033[36m",
    "magenta": "\033[35m",
    "white": "\033[37m",
    "black": "\033[30m",
    "bg_red": "\033[41m",
    "bg_green": "\033[42m",
    "bg_blue": "\033[44m",
    "bg_yellow": "\033[43m",
    "bg_cyan": "\033[46m",
    "bg_magenta": "\033[45m",
    "bg_white": "\033[47m",
    "bg_black": "\033[40m",
    "bold": "\033[1m",
    "underline": "\033[4m",
    "reset": "\033[0m"
}

def setcolor(color):
    if color not in COLORS:
        print(f"Error: color '{color}' not found")
        return
    print(COLORS[color], end="")

def reset():
    print(COLORS["reset"], end="")

def show_colors():
    print("\n ==)) READY COLOR ==)) \n")
    for name, code in COLORS.items():
        if name != "reset":
            print(f"{code}{name}{COLORS['reset']}")
    print()