import pygame
import sys

#initialize pygame
pygame.init()
clock = pygame.time.Clock()

#setup display
WIDTH , HEIGHT = 1600 , 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("rotation Simulator")

#setup color and font
green = (255,0,0)
white = (255,255,255)
blue = (0,0,255)
font = pygame.font.Font('freesansbold.ttf',32)
font_pause = pygame.font.Font('freesansbold.ttf',60)
paused = False

#setup physics
nita = 1.18 * pow(10,-5)
nita_water = 0.89 *pow(10,-3)
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

#ball with water resistance
mass_water_resistance = 10
radius_water_resistance = 20
pos_x_water_resistance = WIDTH//2 -50
pos_y_water_resistance = radius_water_resistance
speed_water_resistance = 0

#main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
    

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
    
    if not paused:

        #update speed and position
        speed += gravity
        nita_acc = 6*3.14*nita*radius*speed/mass
        if speed > 0:
            speed -= nita_acc
            net_acc = gravity-nita_acc
            net_acc_rounded = round(net_acc,2)
        elif speed < 0:
            speed += nita_acc
            net_acc = gravity+nita_acc
            net_acc_rounded = round(net_acc,4)
        pos_y += speed
        rounded_speed = round(speed,2)

        #udate position forball without air resistance
        speed_without_air_resistance += gravity
        pos_y_without_air_resistance += speed_without_air_resistance
        rounded_speed_without_air_resistance = round(speed_without_air_resistance,2)

        #water resistance update
        speed_water_resistance += gravity
        nita_water_acc = 6*3.14*nita_water*radius_water_resistance*speed_water_resistance
        if speed_water_resistance > 0:
            speed_water_resistance -= nita_water_acc
            net_acc_water = gravity-nita_water_acc
        elif speed_water_resistance < 0:
            speed_water_resistance += nita_water_acc
            net_acc_water = gravity + nita_water_acc
        pos_y_water_resistance += speed_water_resistance
        rounded_speed_water = round(speed_water_resistance,2)


    #check for collision
    if pos_y > collision_surface:
        pos_y = collision_surface
        speed = -speed * restitution
    if pos_y_without_air_resistance > collision_surface:
        pos_y_without_air_resistance = collision_surface
        speed_without_air_resistance = -speed_without_air_resistance*restitution
    if pos_y_water_resistance > collision_surface:
        pos_y_water_resistance = collision_surface
        speed_water_resistance = -speed_water_resistance*restitution

    #print paused
    pause_text = font_pause.render("PAUSED",True,(0,0,0))if paused else font.render("",True,(0,0,0))
    screen.blit(pause_text,(WIDTH//2-120,30))

    #print speeds
    speed_text = font.render(f"Speed with air resistance: {rounded_speed}",True,(0,0,0))
    speed_water_resistance_text = font.render(f"speed with water resistance: {rounded_speed_water}",True,(0,0,0))
    speed_without_air_resistance_text = font.render(f"speed without air resistance: {rounded_speed_without_air_resistance}",True,(0,0,0))
    screen.blit(speed_text,(20,30))
    screen.blit(speed_without_air_resistance_text,(20,110))
    screen.blit(speed_water_resistance_text,(20,190))

    #print net acceleration
    net_accl_without_air_resistance =font.render(f"net acc. without air resistance: {gravity}",True,(0,0,0))
    net_accl_with_air_resistance = font.render(f"net acc. with air resistance: {net_acc_rounded}",True,(0,0,0))
    net_accl_water_resistance = font.render(f"net acc. with water resistance: {round(net_acc_water,2)}",True,(0,0,0))
    screen.blit(net_accl_without_air_resistance,(20, 150))
    screen.blit(net_accl_with_air_resistance,(20,70))
    screen.blit(net_accl_water_resistance,(20,230))

    #draw the circle
    pygame.draw.circle(screen, (64,64,64),(pos_x,pos_y), radius)
    pygame.draw.circle(screen,(66,53,255),(pos_x_water_resistance,pos_y_water_resistance),radius_water_resistance )
    pygame.draw.circle(screen, (53,255,53), (pos_x_without_air_resistance, pos_y_without_air_resistance), radius_without_air_resistance)

    #update the screen
    pygame.display.flip()
    clock.tick(1)
