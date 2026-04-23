from colors import COLORS, setcolor, reset

def test_color():
    assert "red" in COLORS
    assert "bg_blue" in COLORS
    assert "bold" in COLORS
    assert "reset" in COLORS

def test_reset():
    assert COLORS["reset"] == "\033[0m"

def test_bad():
    setcolor("badcolor")