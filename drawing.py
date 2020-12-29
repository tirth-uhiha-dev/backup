import pygame
#intializng the pygame
pygame.init()

#making the drawing window in which we will code
screen = pygame.display.set_mode((900 , 700))

#this variable will turn false when the quit button is pressed
running = True

#rgb color value for the rectange and the drawing window
white = (0 , 255 , 255)
black = (0,0,0)
red = (255,0,0)
#x and y cordinates for the rectangle postion and the moving algorithm
# rec_y = 400
# rec_x = 300
rec_x_change = 1
rec_y_change = 1
clock = pygame.time.Clock()
rec_size =pygame.draw.rect(screen , black,[rec_x_change, rec_y_change ,10,10])





posCache = [[1,2]]

#drawing loop and the drawing loop
while running:
    screen.fill((white))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #event if a key is pressend than do this
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            rec_x_change += -3
            
        if event.key == pygame.K_RIGHT:
           rec_x_change += 3
           

        if event.key == pygame.K_UP:
            rec_y_change += -3

        if event.key == pygame.K_DOWN:
            rec_y_change += 3
        while True:    
            posCache.append([rec_x_change,  rec_y_change])
            if event.key == pygame.K_TAB:   
                for x,y in posCache:
                    pygame.draw.rect(screen, red,[x, y ,10,10])
            break


    #rectangle 
    pygame.draw.rect(screen , black,[rec_x_change, rec_y_change ,10,10])
    #creating a boundry
    if rec_x_change <0:
        rec_x_change = 3
        rec_x_change += rec_y_change
    elif rec_x_change >= 890:
        rec_x_change = 890

    #frames per second
    clock.tick(80)


    pygame.display.flip()           
