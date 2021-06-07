import unittest
from game import TicTacToe


class TestWinner(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_winner(self):
        self.game.board = ['X', 'X', 'X', ' ', 'O', ' ', ' ', ' ', ' ']
        self.assertTrue(self.game.winner(0, 'X'))
        self.assertTrue(self.game.winner(1, 'X'))
        self.assertTrue(self.game.winner(2, 'X'))
        self.assertFalse(self.game.winner(5, 'O'))

        self.game.board = [' ', 'O', ' ', 'X', ' ', ' ', 'X', 'X', 'X']
        self.assertTrue(self.game.winner(8, 'X'))
        self.assertTrue(self.game.winner(7, 'X'))
        self.assertTrue(self.game.winner(6, 'X'))
        self.assertFalse(self.game.winner(3, 'X'))
        self.assertFalse(self.game.winner(1, 'O'))

        self.game.board = ['X', 'O', ' ', 'X', ' ', ' ', 'X', 'O', ' ']
        self.assertTrue(self.game.winner(0, 'X'))
        self.assertTrue(self.game.winner(3, 'X'))
        self.assertTrue(self.game.winner(6, 'X'))
        self.assertFalse(self.game.winner(1, 'O'))
        self.assertFalse(self.game.winner(7, 'O'))

        self.game.board = ['O', ' ', 'X', 'X', ' ', 'X', 'O', ' ', 'X']
        self.assertTrue(self.game.winner(2, 'X'))
        self.assertFalse(self.game.winner(3, 'X'))
        self.assertTrue(self.game.winner(5, 'X'))
        self.assertTrue(self.game.winner(8, 'X'))
        self.assertFalse(self.game.winner(0, 'O'))
        self.assertFalse(self.game.winner(6, 'O'))

        self.game.board = ['O', ' ', ' ', 'X', 'O', 'X', ' ', ' ', 'O']
        self.assertTrue(self.game.winner(0, 'O'))
        self.assertTrue(self.game.winner(4, 'O'))
        self.assertTrue(self.game.winner(8, 'O'))
        self.assertFalse(self.game.winner(3, 'X'))
        self.assertFalse(self.game.winner(5, 'X'))


if __name__ == '__main__':
    unittest.main()
