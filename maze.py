import pygame
from constants import WHITE

def load_maze():
    maze = []
    with open('labirinto.txt', 'r') as file:
        for line in file:
            row = line.strip().split(",")
            maze.append(row)
    return maze

# Função para desenhar o labirinto na tela
def draw_maze(screen, maze):
    block_size = 10
    blocks = []
    block_image = pygame.image.load('assets/wall_orginal.bmp')  # Carrega a imagem do asset
    block_image = pygame.transform.scale(block_image, (block_size, block_size))  # Redimensiona a imagem para o tamanho do bloco
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if cell == '1':
                rect = pygame.Rect(x * block_size, y * block_size, block_size, block_size)
                blocks.append(rect)
                screen.blit(block_image, rect)  # Desenha a imagem do asset em vez de um retângulo
    return blocks
