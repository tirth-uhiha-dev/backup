import pygame
import random

pygame.init()

# creating a game window
screen = pygame.display.set_mode((900, 800))

# giving a title to our screen
pygame.display.set_caption("some random game")


# CREATING colors for the window and other objects
white = (
    0,
    0,
    0,
)
red = (255, 0, 0)
green = (0, 0, 255)

# creating a varialble which will trun fasle when we press quit button on the button
running = True

# varialbles of the rectangle
rec_x = 10
rec_y = 10
rec_x_change = 0
rec_y_change = 0

# variables of the cars
car_x = random.randint(0, 800)
car_y = random.randint(50, 150)
car_x_change = 0.3
car_y_change = 40
carImage = pygame.image.load("ufo.png")
# functiion for the car
def car(x, y):
    screen.blit(carImage, (x, y)) 


posCache = []

# our main game loop
while running:
    screen.fill((0, 0, 0))
    # this for loop here will stop the code when the quit button is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # moving the rectangle left hand-side algoritm
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rec_x_change -= 20
            # moving the rectangle right hand-side algorithm
            if event.key == pygame.K_RIGHT:
                rec_x_change += 60

            if event.key == pygame.K_UP:
                rec_y_change =+ -10

            if event.key == pygame.K_DOWN:
                rec_y_change =+ 10
        posCache.append([rec_x_change,  rec_y_change])
        for x,y in posCache:
            pygame.draw.rect(screen, green, (x,y, 30, 30))


           
    #defining the cars logice to move aroung in the map
    car_x += car_x_change
    if car_x <= 0.3:
        car_x_change = 0.3
        car_y += car_y_change

    elif car_x >= 736:
        car_x_change = -0.3
        car_y += car_y_change

    board = ["-","-","-",
            "-","-","-",
            "-","-","-"]
    def maze(x , y):
        
        print(board[0] + '|' + board[1] + '|' + board[2] + "  1|2|3")
        print(board[3] + '|' + board[4] + '|' + board[5] + "  4|5|6")
        print(board[6] + '|' + board[7] + '|' + board[8] + "  7|8|7")
        

    
     


    pygame.draw.rect(screen, green, (rec_x_change, rec_y_change, 30, 30))
    car(car_x, car_y)
    pygame.display.flip()
    pygame.display.update()
