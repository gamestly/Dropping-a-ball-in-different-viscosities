import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Fall Simulation")

# Set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# Set up player variables
player_size = 50
player_x = width // 2 - player_size // 2
player_y = 0
player_speed = 0  # Initial speed
gravity = 0.5    # Acceleration due to gravity
collision_surface = height - player_size  # Surface where the player will bounce
bounce_damping = 0.5  # Damping factor for rebound

# Set up clock
clock = pygame.time.Clock()

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Handle user input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < width - player_size:
        player_x += player_speed

    # Update player position (fall simulation)
    player_speed += gravity  # Acceleration due to gravity
    player_y += player_speed

    # Check for collision with the surface
    if player_y > collision_surface:
        player_y = collision_surface
        player_speed = -player_speed * bounce_damping  # Rebound with damping

    # Draw everything
    screen.fill(black)
    pygame.draw.rect(screen, white, (player_x, player_y, player_size, player_size))

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
