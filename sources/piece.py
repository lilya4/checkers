import pygame
from .constants import RED, SQUARE_SIZE, WHITE, YELLOW, CROWN


class Piece:
    PADDING = 15
    def __init__(self, row, col, color):
        self.x = SQUARE_SIZE * col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * (7 - row) + SQUARE_SIZE // 2
        self.color = color
        self.is_king = False

    def draw(self, display, is_selected):
        radius = SQUARE_SIZE // 2 - self.PADDING
        if is_selected:
            pygame.draw.circle(display, YELLOW, (self.x, self.y), radius)
        else:
            pygame.draw.circle(display, self.color, (self.x, self.y), radius)
        if self.is_king:
            display.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))
    def move(self, row, col):
        self.x = SQUARE_SIZE * col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * (7 - row) + SQUARE_SIZE // 2
        if row == 7 and self.color == WHITE or row == 0 and self.color == RED:
            self.is_king = True