import sys
from colors import setcolor, reset, show_colors

def main():
    args = sys.argv[1:]

    if not args:
        print("terminal_color <цвет>")
        print("terminal_color --list")
        print("terminal_color --reset")
        return
    
    cmd = args[0]

    if cmd == "--list":
        show_colors()
    elif cmd == "--reset":
        reset()
    else:
        setcolor(cmd)

if __name__ == "__main__":
    main()