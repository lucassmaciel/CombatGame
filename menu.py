import pygame
import sys
from button import Button
from main import main

pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

WIDTH, HEIGHT = 720, 480
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Combat Game")

BG = pygame.image.load("assets/Background.png")
surface = pygame.display.set_mode((WIDTH, HEIGHT))

def get_font(size):
    return pygame.font.Font("assets/font.ttf", size)

def play():
    main()


def main_menu():
    screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(40).render("MAIN MENU", True, WHITE)
        MENU_RECT = MENU_TEXT.get_rect(center=(WIDTH //2 , HEIGHT // 2 - 160))

        PLAYER = Button(image=None, pos=(WIDTH // 2, HEIGHT // 2 - 50),
                                   text_input="PLAY", font=get_font(30), base_color=WHITE,
                                   hovering_color="green")

        INSTRUCTIONS = Button(image=None, pos=(WIDTH // 2, HEIGHT // 2 + 50),
                                   text_input="INSTRUCTIONS", font=get_font(25), base_color=WHITE,
                                   hovering_color="green")

        QUIT_BUTTON = Button(image=None, pos=(WIDTH // 2, HEIGHT - 100), text_input="QUIT", font=get_font(30),
                             base_color=WHITE, hovering_color="green")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAYER, INSTRUCTIONS, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAYER.checkForInput(MENU_MOUSE_POS):
                    pygame.time.delay(200)
                    play()
                if INSTRUCTIONS.checkForInput(MENU_MOUSE_POS):
                    pygame.time.delay(200)
                    font = get_font(30)
                    text1 = font.render("PLAYER 1: Use WASD keys to move, SPACE to shoot", True, WHITE)
                    text2 = font.render("PLAYER 2: Use arrow keys to move, ENTER to shoot", True, WHITE)
                    
                    screen.fill((0, 0, 0))  # preenche a tela com preto
                    screen.blit(text1, (50, 50))
                    screen.blit(text2, (50, 100))
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
            elif event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
if __name__ == "__main__":
    while True:
        main_menu()
