import pygame, sys

pygame.init()

display_width = 500
display_height = 500

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Maze Game')

black = (0, 0, 0)
white = (255, 255, 255)

Player = pygame.image.load("ball.png")





def ball(x,y):
    gameDisplay.blit(Player, (x,y))

x = (display_width * 0.4)
y = (display_height * 0.4)
x_change = 0
y_change = 0

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                y_change = 5
            elif event.key == pygame.K_UP:
                y_change = -5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                y_change = 0


    x += x_change
    y += y_change

    gameDisplay.fill(black)
    ball(x,y)

    pygame.display.update()


pygame.quit()
quit()
