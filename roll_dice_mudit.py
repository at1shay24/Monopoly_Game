import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen setup
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Turn Based Dice Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (70, 130, 180)

# Fonts
font = pygame.font.SysFont(None, 40)
emoji_font = pygame.font.SysFont("Segoe UI Emoji", 100)  # supports dice emojis

# Dice emoji faces
dice_emojis = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

# Players
players = ["Mudit", "Atishay"]
current_player_index = 0
dice_result = None

# Button
roll_button = pygame.Rect(WIDTH//2 - 75, HEIGHT - 80, 150, 50)

def draw_screen():
    screen.fill(WHITE)

    # Title
    title = font.render("Dice Roller", True, BLACK)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 20))

    # Current turn
    turn_text = font.render(f"{players[current_player_index]}'s Turn", True, BLACK)
    screen.blit(turn_text, (WIDTH // 2 - turn_text.get_width() // 2, 80))

    # Dice result
    if dice_result is not None:
        dice_text = emoji_font.render(dice_emojis[dice_result - 1], True, BLACK)
        screen.blit(dice_text, (WIDTH // 2 - dice_text.get_width() // 2, 150))

    # Draw button
    pygame.draw.rect(screen, BLUE, roll_button)
    btn_text = font.render("Roll Dice", True, WHITE)
    screen.blit(
        btn_text,
        (
            roll_button.x + (roll_button.width - btn_text.get_width()) // 2,
            roll_button.y + (roll_button.height - btn_text.get_height()) // 2,
        ),
    )

    pygame.display.flip()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if roll_button.collidepoint(event.pos):
                dice_result = random.randint(1, 6)
                current_player_index = (current_player_index + 1) % len(players)

    draw_screen()
