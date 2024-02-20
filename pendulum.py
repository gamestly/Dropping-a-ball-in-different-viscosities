import pygame
import sys
import math

# Pygame initialization
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
ANGLE_INCREMENT = 0.03
G = 9.8  # Acceleration due to gravity

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Pendulum Simulation")

clock = pygame.time.Clock()

# Initial angle, angular velocity, and pendulum length
angle = math.pi / 4  # 45 degrees
angular_velocity = 0.0
pendulum_length = 200

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                pendulum_length += 10
            elif event.key == pygame.K_DOWN:
                pendulum_length -= 10

    # Update angle and angular velocity based on simple pendulum equations
    angular_acceleration = -G / pendulum_length * math.sin(angle)
    angular_velocity += angular_acceleration
    angle += angular_velocity

    # Clear the screen
    screen.fill(BLACK)

    # Calculate the position of the pendulum bob
    bob_x = WIDTH // 2 + int(pendulum_length * math.sin(angle))
    bob_y = HEIGHT // 4 + int(pendulum_length * math.cos(angle))

    # Draw the pendulum rod
    pygame.draw.line(screen, WHITE, (WIDTH // 2, HEIGHT // 4), (bob_x, bob_y), 2)

    # Draw the pendulum bob
    pygame.draw.circle(screen, WHITE, (bob_x, bob_y), 20)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

    # Slow down the simulation for better visualization
    pygame.time.delay(20)
