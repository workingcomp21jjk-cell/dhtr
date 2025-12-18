import pygame
import sys
import time

pygame.init()

# розміри вікна
WIDTH, HEIGHT = 500, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Клікер-гра")

# кольори
WHITE = (255, 255, 255)
BLUE = (70, 130, 180)
DARK_BLUE = (40, 90, 140)
BLACK = (0, 0, 0)

# шрифти
font = pygame.font.SysFont(None, 36)

# кнопка (круг)
button_pos = (WIDTH // 2, HEIGHT // 2)
button_radius = 60

# змінні гри
score = 0
game_time = 30  # секунд
start_time = time.time()
game_over = False

def draw_button(mouse_pos):
    color = DARK_BLUE if pygame.mouse.get_pressed()[0] else BLUE
    pygame.draw.circle(screen, color, button_pos, button_radius)

def draw_text(text, x, y):
    img = font.render(text, True, BLACK)
    screen.blit(img, (x, y))

# головний цикл
while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mx, my = pygame.mouse.get_pos()
            distance = ((mx - button_pos[0])**2 + (my - button_pos[1])**2) ** 0.5
            if distance <= button_radius:
                score += 1

    # таймер
    elapsed = int(time.time() - start_time)
    time_left = game_time - elapsed

    if time_left <= 0:
        game_over = True

    if not game_over:
        draw_button(pygame.mouse.get_pos())
        draw_text(f"Очки: {score}", 20, 20)
        draw_text(f"Час: {time_left}", 380, 20)
    else:
        draw_text("Час вийшов!", 170, 150)
        draw_text(f"Твій результат: {score}", 150, 200)

    pygame.display.update()
