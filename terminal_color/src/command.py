import sys
from colors import COLORS

def gen_ps1(fg=None, bg=None):
    reset = COLORS["reset"]
    fg_code = COLORS.get(fg, "")
    bg_code = COLORS.get(bg, "")
    ps1 = ""
    if fg:
        ps1 += "%{" + fg_code + "%}"
    if bg:
        ps1 += "%{" + bg_code + "%}"
    ps1 += "➜ %n %~"
    ps1 += "%{" + reset + "%}"
    ps1 += "$ "
    return ps1

def main():
    args = sys.argv[1:]
    if not args:
        print("Write for eval:")
        print("  eval \"$(python3 command.py red)\"")
        print("  eval \"$(python3 command.py bg_green)\"")
        print("  eval \"$(python3 command.py --reset)\"")
        print("  python3 command.py --list")
        return

    cmd = args[0]
    if cmd == "--list":
        from colors import show_colors
        show_colors()
        return
    if cmd == "--reset":
        print("export PS1='%n@%m %~ %# '")
        return

    t_colors = ["red","green","blue","yellow","cyan","magenta","white","black"]
    b_colors = ["bg_red","bg_green","bg_blue","bg_yellow","bg_cyan","bg_magenta","bg_white","bg_black"]
    if cmd in t_colors:
        ps1 = gen_ps1(fg=cmd)
        print(f"export PS1='{ps1}'")
    elif cmd in b_colors:
        ps1 = gen_ps1(bg=cmd)
        print(f"export PS1='{ps1}'")
    elif cmd in ("bold","underline"):
        sys.stdout.write(COLORS[cmd])
        sys.stdout.flush()
    else:
        print(f"echo 'NO this color: {cmd}'")

if __name__ == "__main__":
    main()