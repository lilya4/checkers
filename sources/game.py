import pygame
from .board import Board
from .constants import RED, WHITE


class Game:
    def __init__(self, display):
        self.board = Board()
        self.display = display
        self.selected_piece = None
        self.turn = WHITE
        self.possible_moves = []

    def update(self):
        self.board.draw(self.display, self.selected_piece, self.possible_moves)
        pygame.display.update()

    def no_winner(self):
        return self.board.winner() is None

    def select(self, row, col):
        if (self.selected_piece is not None) and ((row, col) in self.possible_moves):
            self.board.move(self.selected_piece, row, col, self.turn)
            self.selected_piece = None
            self.possible_moves = []
            if self.turn == WHITE:
                self.turn = RED
            else:
                self.turn = WHITE
        else:
            self.possible_moves = []
            if self.board.pieces[row][col] != 0:
                if self.board.pieces[row][col].color == self.turn:
                    self.selected_piece = row, col
                    if self.board.pieces[row][col].is_king:  #ищем возможные ходы
                        next_row = row
                        next_col = col
                        killed = False
                        for i in range(-1, 2, 2):
                            for j in range(-1, 2, 2):
                                while 7 >= next_row + i >= 0 and 7 >= next_col + j >= 0:
                                    next_row += i
                                    next_col += j
                                    if self.board.pieces[next_row][next_col] != 0:
                                        if self.board.pieces[next_row][next_col].color == self.turn:
                                            break
                                        if killed:
                                            break
                                        killed = True
                                    elif self.board.pieces[next_row][next_col] == 0:
                                        self.possible_moves.append((next_row, next_col))
                                next_row = row
                                next_col = col
                                killed = False
                    else:
                        for i in range(-1, 2, 2):
                            for j in range(-1, 2, 2):
                                going_forward = i > 0 and self.turn == WHITE or i < 0 and self.turn == RED
                                if going_forward and 7 >= row + i >= 0 and 7 >= col + j >= 0 and \
                                        self.board.pieces[row + i][col + j] == 0:
                                    self.possible_moves.append((row + i, col + j))
                                if 7 >= row + 2 * i >= 0 and 7 >= col + 2 * j >= 0 and \
                                        self.board.pieces[row + i][col + j] != 0 and \
                                        self.board.pieces[row + i][col + j].color != self.turn and \
                                        self.board.pieces[row + 2 * i][col + 2 * j] == 0:
                                    self.possible_moves.append((row + 2 * i, col + 2 * j))
            else:
                self.selected_piece = None
                self.possible_moves = []
