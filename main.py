import pygame
from pygame.locals import *
from maze import draw_maze, load_maze
from player import Player
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Combat_atari")
clock = pygame.time.Clock()


def main():
    maze = load_maze()
    players = pygame.sprite.Group()
    bullets = pygame.sprite.Group()

    player1_x, player1_y = 50, 210
    player2_x, player2_y = 650, 210

    player1 = Player(player1_x, player1_y, {'up': K_w, 'down': K_s, 'left': K_a, 'right': K_d})
    player2 = Player(
        player2_x, player2_y, {'up': K_UP, 'down': K_DOWN, 'left': K_LEFT, 'right': K_RIGHT})

    players.add(player1, player2)

    for player in players:
        player.bullets.draw(screen)

    running = True
    while running:
        screen.fill((0, 0, 0))
        blocks = draw_maze(screen, maze) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player1.shoot()
                elif event.key == pygame.K_RETURN:
                    player2.shoot()

        for bullet in bullets:
            bullet.update(blocks, players)

        player1.update(players, blocks)
        player2.update(players, blocks)

        players.draw(screen)
        bullets.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()