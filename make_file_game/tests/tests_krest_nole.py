from src.krest_nole import check_win

def test_win_row():
    board = [["X","X","X"],
             ["","",""],
             ["","",""]]
    assert check_win(board, "X") is True

def test_win_col():
    board = [["","O",""],
             ["","O",""],
             ["","O",""]]
    assert check_win(board, "O") is True

def test_win_diag():
    board = [["X","",""],
             ["","X",""],
             ["","","X"]]
    assert check_win(board, "X") is True

def test_no_win():
    board = [["X","O","X"],
             ["O","X","O"],
             ["O","X","O"]]
    assert check_win(board, "X") is False