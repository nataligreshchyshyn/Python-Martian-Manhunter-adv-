from game import TicTacToe


tictac = TicTacToe()
tictac.board = [' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ', ' ']


def test_available_moves():
    assert (4 not in tictac.available_moves())


def test_make_move():
    assert tictac.make_move(4, 'X') is False
    assert tictac.make_move(5, 'X') is True
    assert tictac.board[5] != ' '
