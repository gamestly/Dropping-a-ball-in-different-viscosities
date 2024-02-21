import pygame
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Uniform Circular Motion")
font = pygame.font.Font('freesansbold.ttf',32)

# Set up the circle
circle_radius = 50
circle_color = (255, 0, 0)
center = (width // 2, height // 2)
distance = 100

# Set up the motion parameters
angular_speed = 0.1  # Adjust the angular speed as needed
angle = 0

# Main game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                distance += 10
            if  event.key == pygame.K_DOWN:
                distance -= 10

    # Update angle for circular motion
    angle += angular_speed
    centripetal_accel = distance*(angular_speed**2)

    # Calculate circle position based on polar coordinates
    circle_x = center[0] + (circle_radius + distance) * math.cos(angle)
    circle_y = center[1] + (circle_radius + distance) * math.sin(angle)

    # Clear the screen
    screen.fill((255, 255, 255))

    text_acc = font.render(f"centripetal acceleration: {round(centripetal_accel,2)}m/s2",True,(0,0,0))
    screen.blit(text_acc, (0 ,0))

    # Draw the circle at its current position
    pygame.draw.circle(screen, circle_color, (round(circle_x), round(circle_y)), circle_radius)
    pygame.draw.circle(screen,(0,0,0),(width//2,height//2),3)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
