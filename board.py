from square import Square
from texttable import Texttable
from texttable import bcolors, get_color_string


class Board:

    SIGNS = [get_color_string(bcolors.RED, 'X'), get_color_string(bcolors.BLUE, 'O')]

    def __init__(self):
        self.board = []
        self.create_board()

    def create_board(self, width=3):
        self.board.append([Square(str(i + 1)) for i in range(width)])
        self.board.append([Square(str(i + 4)) for i in range(width)])
        self.board.append([Square(str(i + 7)) for i in range(width)])

    def check_win(self):
        for i in range(3):
            if self.board[0][i].sign == self.board[1][i].sign == self.board[2][i].sign:
                return True
            if self.board[i][0].sign == self.board[i][1].sign == self.board[i][2].sign:
                return True
        if self.board[0][0].sign == self.board[1][1].sign == self.board[2][2].sign:
            return True
        if self.board[0][2].sign == self.board[1][1].sign == self.board[2][0].sign:
            return True
        return False

    def check_draw(self):
        squares = []
        for i in self.board:
            for k in i:
                squares.append(k.sign) if k.sign in Board.SIGNS else squares.append('')
        if all(squares):
            return True
        else:
            return False

    def __str__(self):
        t = Texttable()
        for row in self.board:
            t.add_row(row)
        return t.draw()