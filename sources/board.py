import pygame
from .constants import BLACK, ROWS, RED, SQUARE_SIZE, COLS, WHITE, YELLOW
from .piece import Piece


class Board:
    def __init__(self):
        self.pieces = []
        self.red_left = self.white_left = 12
        for row in range(ROWS):
            self.pieces.append([])
            for col in range(COLS):
                if col % 2 == (row  % 2):
                    if row < 3:
                        self.pieces[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.pieces[row].append(Piece(row, col, RED))
                    else:
                        self.pieces[row].append(0)
                else:
                    self.pieces[row].append(0)

    def winner(self):
        if self.red_left <= 0:
            return WHITE
        elif self.white_left <= 0:
            return RED
        return None

    def draw(self, display, selected_piece, possible_moves):
        display.fill(WHITE)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                if (row, col) in possible_moves:
                    pygame.draw.rect(display, YELLOW,
                                     (col * SQUARE_SIZE, (7 - row) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
                else :
                    pygame.draw.rect(display, BLACK,
                                     (col * SQUARE_SIZE, (7 - row) * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        for row in range(ROWS):  # draw pieces
            for col in range(COLS):
                piece = self.pieces[row][col]
                if piece != 0:
                    piece.draw(display, (row, col) == selected_piece)

    def move(self, selected_piece, row, col, turn):
        prev_row, prev_col = selected_piece
        if abs(prev_row - row) >= 2:
            step_r = 1
            if prev_row > row:
                step_r = -1
            step_c = 1
            if prev_col > col:
                step_c = -1
            for i in range(prev_row + step_r, row, step_r):
                for j in range(prev_col + step_c, col, step_c):
                    if self.pieces[i][j] != 0:
                        self.pieces[i][j] = 0
                        if turn == WHITE:
                            self.red_left -= 1
                        else:
                            self.white_left -= 1
        self.pieces[row][col] = self.pieces[prev_row][prev_col]
        self.pieces[row][col].move(row, col)
        self.pieces[prev_row][prev_col] = 0
