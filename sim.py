import pygame
import sys
import time
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
G = 0.1  # Gravitational constant
MASS = 1000  # Mass of the planet

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Function to calculate gravitational force between two objects
def calculate_gravity(mass1, mass2, distance):
    force = G * (mass1 * mass2) / (distance ** 2)
    return force

# Function to update the position and velocity of the planet
def update_position_velocity(position, velocity, acceleration):
    velocity[0] += acceleration[0]
    velocity[1] += acceleration[1]
    position[0] += velocity[0]
    position[1] += velocity[1]

# Create Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Planet Simulation")

# Initial position, velocity, and acceleration of the planet
planet_position = [WIDTH // 2, HEIGHT // 2]
planet_velocity = [0, 0]
planet_acceleration = [0, 0]

clock = pygame.time.Clock()

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Calculate distance between the planet and the center of the screen
    distance = math.sqrt(
        (planet_position[0] - WIDTH // 2) ** 2 + (planet_position[1] - HEIGHT // 2) ** 2
    )

    # Avoid division by zero by checking if the distance is non-zero
    if distance != 0:
        # Calculate gravitational force
        force = calculate_gravity(MASS, 1, distance)

        # Calculate acceleration components
        acceleration_x = force * (WIDTH // 2 - planet_position[0]) / distance
        acceleration_y = force * (HEIGHT // 2 - planet_position[1]) / distance
        planet_acceleration = [acceleration_x, acceleration_y]

        # Update position and velocity
        update_position_velocity(planet_position, planet_velocity, planet_acceleration)

    # Clear the screen
    screen.fill(BLACK)

    # Draw the planet
    pygame.draw.circle(screen, WHITE, (int(planet_position[0]), int(planet_position[1])), 10)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)
