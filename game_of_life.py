import pygame
import sys

WIDTH = 800
ROWS = 20
WIN = pygame.display.set_mode((WIDTH, WIDTH))

pygame.display.set_caption("Game of Life")

# RGB Values of the Nodes
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Node:
    def __init__(self, row, col, width):
        self.row = row
        self.col = col
        self.x = int(row * width)
        self.y = int(col * width)
        self.color = WHITE
        self.occupied = None
    
    def draw(self, WIN):
        pygame.draw.rect(WIN, self.color, (self.x, self.y, WIDTH//8, WIDTH//8))
    
    def make_grid(rows, width):
        grid = []
        gap = WIDTH // rows
        print(gap)
        for i in range(rows):
            grid.append([])
            for j in range(rows):
                node = Node(j, i, gap)
            grid[i].append(node)
        return grid
    
    def draw_grid(win, rows, width):
        gap = width // ROWS
        for i in range(rows):
            pygame.draw.line(win, BLACK, (0, i*gap), (width, i*gap))
            for j in range(rows):
                pygame.draw.line(win, BLACK, (j * gap, 0), (j * gap, width))