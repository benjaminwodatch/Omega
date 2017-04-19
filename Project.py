import pygame, sys
from pygame.locals import *

display_width = 500
display_height = 500
black = (0, 0, 0)
white = (255, 255, 255)


class Ball(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, pos):
       # Call the parent class (Sprite) constructor
       pygame.sprite.Sprite.__init__(self)

       # Create an image of the block, and fill it with a color.
       # This could also be an image loaded from the disk.
       self.image = pygame.image.load("ball.png")

       # Fetch the rectangle object that has the dimensions of the image
       # Update the position of this object by setting the values of rect.x and rect.y
       self.rect = self.image.get_rect()

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Maze Game")

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((white))

    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Hello There", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    textpos.centery = background.get_rect().centery
    background.blit(text, textpos)

    ball = Ball((30, 30))
    ballsprite = pygame.sprite.RenderPlain(ball)
    # Blit everything to the screen
    screen.blit(background, (0, 0))

    pygame.display.flip()
    clock = pygame.time.Clock()
    # Event loop
    while 1:

        clock.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                return


        screen.blit(background, ball.rect, ball.rect)
        ballsprite.update()
        ballsprite.draw(screen)
        pygame.display.flip()


if __name__ == '__main__': main()




# display_width = 500
# display_height = 500
#
# gameDisplay = pygame.display.set_mode((display_width,display_height))
# pygame.display.set_caption('Maze Game')
#
# black = (0, 0, 0)
# white = (255, 255, 255)
#
# Player = pygame.image.load("ball.png")
#
#
#
#
#
# def ball(x,y):
#     gameDisplay.blit(Player, (x,y))
#
# x = (display_width * 0.4)
# y = (display_height * 0.4)
# x_change = 0
# y_change = 0
#
# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: sys.exit()
#
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_LEFT:
#                 x_change = -5
#             elif event.key == pygame.K_RIGHT:
#                 x_change = 5
#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                 x_change = 0
#
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_DOWN:
#                 y_change = 5
#             elif event.key == pygame.K_UP:
#                 y_change = -5
#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
#                 y_change = 0
#
#
#     x += x_change
#     y += y_change
#
#     gameDisplay.fill(black)
#     ball(x,y)
#
#     pygame.display.update()
#
#
# pygame.quit()
# quit()
