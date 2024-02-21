import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60

# Particle class for fluid simulation
class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.density = 0
        self.pressure = 0

    def update(self):
        # Update particle position
        self.x += self.vx
        self.y += self.vy

# SPH fluid simulation class
class FluidSimulation:
    def __init__(self):
        self.particles = [Particle(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(100)]

    def update(self):
        for particle in self.particles:
            # Update particle position
            particle.update()

    def draw(self, screen):
        for particle in self.particles:
            pygame.draw.circle(screen, (0, 0, 255), (int(particle.x), int(particle.y)), 3)

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fluid Simulation")
clock = pygame.time.Clock()

# Create fluid simulation
fluid_simulation = FluidSimulation()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update fluid simulation
    fluid_simulation.update()

    # Draw particles
    screen.fill((255, 255, 255))
    fluid_simulation.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
