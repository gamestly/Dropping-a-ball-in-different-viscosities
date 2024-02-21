import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Gravitational Rotation Simulation (Three Bodies)")

# Define colors
white = (255, 255, 255)
yellow = (255, 255, 0)
blue = (0, 0, 255)
green = (0, 255, 0)

# Define the celestial bodies
sun_mass = 10000
sun_radius = 30
sun_position = [width // 2, height // 2]
sun_velocity = [0, 0]

planet1_mass = 10
planet1_radius = 15
planet1_position = [width // 2 + 150, height // 2]
planet1_velocity = [0, 3]

planet2_mass = 8
planet2_radius = 12
planet2_position = [width // 2 - 200, height // 2]
planet2_velocity = [0, -2]

# Gravitational constant
G = 0.1

# Time step
dt = 0.1

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate gravitational forces on planet1
    dx1 = sun_position[0] - planet1_position[0]
    dy1 = sun_position[1] - planet1_position[1]
    distance1 = math.sqrt(dx1**2 + dy1**2)
    force_magnitude_sun1 = (G * sun_mass * planet1_mass) / (distance1**2)
    force_angle_sun1 = math.atan2(dy1, dx1)

    force_magnitude_planet2 = (G * planet2_mass * planet1_mass) / (distance1**2)
    force_angle_planet2 = math.atan2(planet2_position[1] - planet1_position[1], planet2_position[0] - planet1_position[0])

    # Update planet1's velocity based on the gravitational forces
    planet1_velocity[0] += (force_magnitude_sun1 * math.cos(force_angle_sun1) + force_magnitude_planet2 * math.cos(force_angle_planet2)) * dt
    planet1_velocity[1] += (force_magnitude_sun1 * math.sin(force_angle_sun1) + force_magnitude_planet2 * math.sin(force_angle_planet2)) * dt

    # Update planet1's position based on its velocity
    planet1_position[0] += planet1_velocity[0] * dt
    planet1_position[1] += planet1_velocity[1] * dt

    # Calculate gravitational forces on planet2
    dx2_sun = sun_position[0] - planet2_position[0]
    dy2_sun = sun_position[1] - planet2_position[1]
    distance2_sun = math.sqrt(dx2_sun**2 + dy2_sun**2)
    force_magnitude_sun2 = (G * sun_mass * planet2_mass) / (distance2_sun**2)
    force_angle_sun2 = math.atan2(dy2_sun, dx2_sun)

    force_magnitude_planet1 = (G * planet1_mass * planet2_mass) / (distance2_sun**2)
    force_angle_planet1 = math.atan2(planet1_position[1] - planet2_position[1], planet1_position[0] - planet2_position[0])

    # Update planet2's velocity based on the gravitational forces
    planet2_velocity[0] += (force_magnitude_sun2 * math.cos(force_angle_sun2) + force_magnitude_planet1 * math.cos(force_angle_planet1)) * dt
    planet2_velocity[1] += (force_magnitude_sun2 * math.sin(force_angle_sun2) + force_magnitude_planet1 * math.sin(force_angle_planet1)) * dt

    # Update planet2's position based on its velocity
    planet2_position[0] += planet2_velocity[0] * dt
    planet2_position[1] += planet2_velocity[1] * dt

    # Calculate gravitational forces on sun
    force_magnitude_sun1 = (G * planet1_mass * sun_mass) / (distance1**2)
    force_magnitude_sun2 = (G * planet2_mass * sun_mass) / (distance2_sun**2)

    # Update sun's velocity based on the gravitational forces
    sun_velocity[0] += (-force_magnitude_sun1 * math.cos(force_angle_sun1) - force_magnitude_sun2 * math.cos(force_angle_sun2)) * dt
    sun_velocity[1] += (-force_magnitude_sun1 * math.sin(force_angle_sun1) - force_magnitude_sun2 * math.sin(force_angle_sun2)) * dt

    # Update sun's position based on its velocity
    sun_position[0] += sun_velocity[0] * dt
    sun_position[1] += sun_velocity[1] * dt

    # Clear the screen
    screen.fill(white)

    # Draw the celestial bodies
    pygame.draw.circle(screen, yellow, (round(sun_position[0]), round(sun_position[1])), sun_radius)
    pygame.draw.circle(screen, blue, (round(planet1_position[0]), round(planet1_position[1])), planet1_radius)
    pygame.draw.circle(screen, green, (round(planet2_position[0]), round(planet2_position[1])), planet2_radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()
