import pygame
import random
import sys

# Define colors
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN=(90, 252, 3)

# Define constants
CELL_SIZE = 30
MARGIN = 5
FONT_SIZE = 20
WIDTH = 10
HEIGHT = 10
NUM_MINES = 10


class Minesweeper:
    def __init__(self, rows, cols, num_mines):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]
        self.visible = [[False for _ in range(cols)] for _ in range(rows)]
        self.flagged = [[False for _ in range(cols)] for _ in range(rows)]
        self.mines = set()
        self.game_over = False
        self.win = False

        self._place_mines()
        self._compute_adjacent_mines()

    def _place_mines(self):
        positions = [(i, j) for i in range(self.rows) for j in range(self.cols)]
        self.mines = set(random.sample(positions, self.num_mines))

    def _compute_adjacent_mines(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if (i, j) in self.mines:
                    continue

                num_adjacent_mines = 0
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        ni, nj = i + di, j + dj
                        if ni >= 0 and ni < self.rows and nj >= 0 and nj < self.cols:
                            if (ni, nj) in self.mines:
                                num_adjacent_mines += 1
                self.board[i][j] = num_adjacent_mines

    def _reveal_square(self, i, j):
        if self.flagged[i][j]:
            return

        if (i, j) in self.mines:
            self.visible[i][j] = True
            self.game_over = True
        elif not self.visible[i][j]:
            self.visible[i][j] = True
            if self.board[i][j] == 0:
                for di in [-1, 0, 1]:
                    for dj in [-1, 0, 1]:
                        ni, nj = i + di, j + dj
                        if ni >= 0 and ni < self.rows and nj >= 0 and nj < self.cols:
                            self._reveal_square(ni, nj)

    def _toggle_flag(self, i, j):
        if not self.visible[i][j]:
            self.flagged[i][j] = not self.flagged[i][j]

    def _check_win(self):
        num_revealed = sum(sum(row) for row in self.visible)
        if num_revealed == self.rows * self.cols - self.num_mines:
            self.win = True

    def handle_mouse_click(self, row, col, button):
        if self.game_over or self.win:
            return

        if button == 1:
            self._reveal_square(row, col)
            if self.game_over:
                self._reveal_mines()
        elif button == 3:
            self._toggle_flag

# Define constants
SCREEN_WIDTH = (CELL_SIZE + MARGIN) * WIDTH + MARGIN
SCREEN_HEIGHT = (CELL_SIZE + MARGIN) * HEIGHT + MARGIN
BG_COLOR = GRAY

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Minesweeper")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, FONT_SIZE)

game = Minesweeper(HEIGHT, WIDTH, NUM_MINES)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            row = pos[1] // (CELL_SIZE + MARGIN)
            col = pos[0] // (CELL_SIZE + MARGIN)
            button = event.button
            game.handle_mouse_click(row, col, button)

    screen.fill(BG_COLOR)

    # Draw board
    for row in range(game.rows):
        for col in range(game.cols):
            x = col * (CELL_SIZE + MARGIN) + MARGIN
            y = row * (CELL_SIZE + MARGIN) + MARGIN

            # Draw visible squares
            if game.visible[row][col]:
                if (row, col) in game.mines:
                    pygame.draw.rect(screen, RED, (x, y, CELL_SIZE, CELL_SIZE))
                else:
                    num_adjacent_mines = game.board[row][col]
                    if num_adjacent_mines == 0:
                        pygame.draw.rect(screen, WHITE, (x, y, CELL_SIZE, CELL_SIZE))
                    else:
                        text = font.render(str(num_adjacent_mines), True, BLACK)
                        text_rect = text.get_rect(center=(x+CELL_SIZE/2, y+CELL_SIZE/2))
                        pygame.draw.rect(screen, WHITE, (x, y, CELL_SIZE, CELL_SIZE))
                        screen.blit(text, text_rect)
            # Draw flagged squares
            elif game.flagged[row][col]:
                pygame.draw.rect(screen, BLACK, (x, y, CELL_SIZE, CELL_SIZE))
                text = font.render("F", True, RED)
                text_rect = text.get_rect(center=(x+CELL_SIZE/2, y+CELL_SIZE/2))
                screen.blit(text, text_rect)
            # Draw unexplored squares
            else:
                pygame.draw.rect(screen, GREEN, (x, y, CELL_SIZE, CELL_SIZE))

    # Display game over or win message
    if game.game_over:
        text = font.render("Game Over", True, RED)
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        screen.blit(text, text_rect)
    elif game.win:
        text = font.render("You Win!", True, BLACK)
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        screen.blit(text, text_rect)

    pygame.display.flip()
    clock.tick(60)