import pygame
import random
import time  # Import the time module

# Initialize Pygame
pygame.init()

# Game window dimensions
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Breakout Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Paddle settings
paddle_width, paddle_height = 100, 20
paddle = pygame.Rect(WIDTH // 2 - paddle_width // 2, HEIGHT - 50, paddle_width, paddle_height)

# Ball settings
ball_radius = 15
ball_speed_x, ball_speed_y = 250, -250
ball = pygame.Rect(WIDTH // 2 - ball_radius // 2, HEIGHT // 2 - ball_radius // 2, ball_radius, ball_radius)

# Brick settings
brick_row, brick_col = 5, 7
brick_width, brick_height = WIDTH // brick_col, 30
bricks = [pygame.Rect(col * brick_width, row * brick_height, brick_width, brick_height) for row in range(brick_row) for col in range(brick_col)]

# Define the desired frame rate
FPS = 60

# Create a clock object
clock = pygame.time.Clock()

# Game loop
run = True
while run:
    # Start of the loop time
    start_time = time.time()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.move_ip(-10, 0)
    if keys[pygame.K_RIGHT] and paddle.right < WIDTH:
        paddle.move_ip(10, 0)

    # Limit the frame rate
    clock.tick(FPS)

    # End of the loop time and calculating elapsed time
    elapsed_time = time.time() - start_time

    # Update the ball's position based on elapsed time
    ball.move_ip(ball_speed_x * elapsed_time, ball_speed_y * elapsed_time)

    # Ball collision with walls
    if ball.left <= 0 or ball.right >= WIDTH:
        ball_speed_x *= -1
    if ball.top <= 0:
        ball_speed_y *= -1

    # Ball collision with paddle
    if ball.colliderect(paddle):
        ball_speed_y *= -1

    # Ball collision with bricks
    for brick in bricks:
        if ball.colliderect(brick):
            ball_speed_y *= -1
            bricks.remove(brick)
            break

    # Ball falls below paddle
    if ball.bottom >= HEIGHT:
        run = False

    # Drawing
    win.fill(BLACK)
    pygame.draw.rect(win, GREEN, paddle)
    pygame.draw.ellipse(win, RED, ball)
    for brick in bricks:
        pygame.draw.rect(win, BLUE, brick)

    pygame.display.update()

pygame.quit()