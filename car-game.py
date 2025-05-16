import pygame
import sys
import time
pygame.init()
screen_width = 600
screen_height = 737


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pygame Basics")
background_color = (34,139,34)

line_height=80
line_width=10
gap=40
clock=pygame.time.Clock()

lines=[]

for i in range(0,screen_height,line_height + gap):
    lines.append(i)
print(lines)

car=pygame.image.load('image-removebg-preview (2).png')
car=pygame.transform.scale(car,(60,120))

car2=pygame.image.load('image-removebg-preview (3).png')
car2=pygame.transform.scale(car2,(60,120))

car3=pygame.image.load('image-removebg-preview (4).png')
car3=pygame.transform.scale(car3,(80,120))


car_x=221
car_y=500

car2_x=215
car2_y=40

car3_x=315
car3_y=350

left_bound=screen_width//3
right_bound=2*screen_width//3 - car.get_width()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and car_x > 200:
        car_x -= 5

    if keys[pygame.K_RIGHT] and car_x + 55 < 400:
        car_x += 5

    if keys[pygame.K_UP]and car_y + 10> 0:
        car_y -= 2

    if keys[pygame.K_DOWN] and car_y + 135< screen_height:
        car_y += 1


    screen.fill(background_color)
    pygame.draw.rect(screen,(50,50,50),(screen_width//3,0,screen_width//3,screen_height))

    car2_y+=3
    if car2_y>screen_height:
        car2_y=-50
    car3_y+=3
    if car3_y>screen_height:
        car3_y=-10

    for i in range(len(lines)):
        lines[i] += 5
        if lines[i] > screen_height:
            lines[i] =- line_height

        pygame.draw.rect(screen,'white',(screen_width//2 - line_width//2, lines[i], line_width,line_height))

    screen.blit(car2, (car2_x, car2_y))
    screen.blit(car3, (car3_x, car3_y))
    screen.blit(car, (car_x, car_y))

    player_car=pygame.Rect(car_x + 5 ,car_y+5,car.get_width() - 12,car.get_height()-3)
    other_car = pygame.Rect(car2_x +7 , car2_y, car2.get_width()-13, car2.get_height()-5)
    other_car2 = pygame.Rect(car3_x + 15, car3_y, car3.get_width()-30, car3.get_height()-5)

# hit boxes

    # pygame.draw.rect(screen, "white", player_car, 3)
    # pygame.draw.rect(screen, "white", other_car, 3)
    # pygame.draw.rect(screen, "white", other_car2, 3)

    if player_car.colliderect(other_car) or player_car.colliderect(other_car2):
        font=pygame.font.Font(None,72)
        text=font.render('Game Over! ',True,'red')
        screen.blit(text,(145,350))
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit()

    pygame.display.flip()
    clock.tick(40)
