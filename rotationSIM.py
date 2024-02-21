import pygame
import sys
import numpy

#initialize pygame
pygame.init()
clock = pygame.time.Clock()

#setup display
WIDTH , HEIGHT = 800 , 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("rotation Simulator")

#setup color
white = (255,255,255)

#setup physics
nita = 1.18 * pow(10,-5)
gravity = 0.5
restitution = 0.9

#setup circle parameters
mass = 10
radius = 20
pos_x = WIDTH//2
pos_y = radius
speed = 0 #initial speed
collision_surface = HEIGHT - radius

#ball without air resistance
mass_without_air_resistance = 10
radius_without_air_resistance = 20
pos_x_without_air_resistance = WIDTH//2 + 50
pos_y_without_air_resistance = radius
speed_without_air_resistance = 0

#main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    key = pygame.key.get_pressed()
    if key[pygame.K_1]  and pos_y == collision_surface:
        speed += 10
        speed_without_air_resistance += 10
    if key[pygame.K_2]  and pos_y == collision_surface:
        speed += 20
        speed_without_air_resistance += 20
    if key[pygame.K_3]  and pos_y == collision_surface:
        speed += 30
        speed_without_air_resistance += 30
    if key[pygame.K_4]  and pos_y == collision_surface:
        speed += 40
        speed_without_air_resistance += 40
    if key[pygame.K_5]  and pos_y == collision_surface:
        speed += 50
        speed_without_air_resistance += 50
    if key[pygame.K_6]  and pos_y == collision_surface:
        speed += 60
        speed_without_air_resistance += 60
    if key[pygame.K_7]  and pos_y == collision_surface:
        speed += 70
        speed_without_air_resistance += 70
    if key[pygame.K_8]  and pos_y == collision_surface:
        speed += 80
        speed_without_air_resistance += 80
    if key[pygame.K_9]  and pos_y == collision_surface:
        speed += 90
        speed_without_air_resistance += 90

    #clear screen
    screen.fill(white)
    
    #update speed and position
    speed += gravity
    nita_acc = 6*3.14*nita*radius*speed/mass
    speed -= nita_acc
    pos_y += speed

    #udate position forball without air resistance
    speed_without_air_resistance += gravity
    pos_y_without_air_resistance += speed_without_air_resistance

    if pos_y > collision_surface:
        pos_y = collision_surface
        speed = -speed * restitution
    if pos_y_without_air_resistance > collision_surface:
        pos_y_without_air_resistance = collision_surface
        speed_without_air_resistance = -speed_without_air_resistance*restitution

    #draw the circle
    pygame.draw.circle(screen, (0,255,255),(pos_x,pos_y), radius)
    pygame.draw.circle(screen, (0,255,0), (pos_x_without_air_resistance, pos_y_without_air_resistance), radius_without_air_resistance)

    #update the screen
    pygame.display.flip()
    clock.tick(60)
