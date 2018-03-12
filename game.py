from board import Board
from player import Player
from texttable import bcolors, get_color_string
from square import Square
import random
import os
import sys
import time


class Game:

    SQUARES = {'1': [0, 0], '2': [0, 1], '3': [0, 2], '4': [1, 0], '5': [1, 1],
               '6': [1, 2], '7': [2, 0], '8': [2, 1], '9': [2, 2]}
    SIGNS = [get_color_string(bcolors.RED, 'X'), get_color_string(bcolors.BLUE, 'O')]

    def __init__(self):
        self.panel = Board()
        self.human_player = Player(random.choice(Game.SIGNS))
        self.computer_player = Player(Game.SIGNS[0] if self.human_player.sign == Game.SIGNS[1] else Game.SIGNS[1])

    def print_board(self):
        os.system('clear')
        print(self.panel)

    def start(self):
        game_is_over = False
        while not game_is_over:
            self.print_board()
            if self.computer_player.sign == Game.SIGNS[0]:
                self.computer_turn()
                self.player_turn()
            else:
                self.player_turn()
                self.computer_turn()

    def computer_turn(self):
        coords = self.get_coordinates_of_blocking_position()
        if not coords:
            coords = random.choice(list(Game.SQUARES.values()))
            while self.panel.board[coords[0]][coords[1]].sign in Game.SIGNS:
                coords = random.choice(list(Game.SQUARES.values()))
        self.panel.board[coords[0]][coords[1]] = Square(self.computer_player.sign)
        time.sleep(1)
        self.print_board()
        if self.panel.check_win():
            print('Computer win!')
            sys.exit()
        if self.panel.check_draw():
            print('It is a draw!')
            sys.exit()

    def get_coordinates_of_blocking_position(self):
        # Check horizontally
        for k, v in enumerate(self.panel.board):
            v = [i.sign for i in v]
            if len(set(v)) < len(v):
                for c, x in enumerate(v):
                    if x not in Game.SIGNS:
                        return k, c
        # Check diagonally
        v = [self.panel.board[k][k].sign for k in range(3)]
        if len(set(v)) < len(v):
            for c, x in enumerate(v):
                if x not in Game.SIGNS:
                    return c, c
        p = [self.panel.board[2][0].sign, self.panel.board[1][1].sign, self.panel.board[0][2].sign]
        if len(set(p)) < len(p):
            for i, j in zip(range(3), reversed(range(3))):
                if self.panel.board[j][i].sign not in Game.SIGNS:
                    return j, i
        # Check vertically
        positions = []
        for i in range(3):
            positions.append([self.panel.board[k][i].sign for k in range(3)])
        for i, v in enumerate(positions):
            if len(set(v)) < len(v):
                for c, x in enumerate(v):
                    if x not in Game.SIGNS:
                        return c, i

    def player_turn(self):
        sign_placed = False
        while not sign_placed:
            user_input = input('Select a space: ')
            if user_input in Game.SQUARES.keys():
                coords = Game.SQUARES[user_input]
            else:
                print('There is no such space!')
                continue
            if self.panel.board[coords[0]][coords[1]].sign not in Game.SIGNS:
                self.panel.board[coords[0]][coords[1]] = Square(self.human_player.sign)
                sign_placed = True
                self.print_board()
                if self.panel.check_win():
                    print('You win!')
                    sys.exit()
                if self.panel.check_draw():
                    print('It is a draw!')
                    sys.exit()
            else:
                print('Space is already taken!')

    def check_draw(self):
        squares = []
        for i in self.panel.board:
            for k in i:
                squares.append(k.sign) if k.sign in Game.SIGNS else squares.append('')

        if all(squares):
            return True
        else:
            return False