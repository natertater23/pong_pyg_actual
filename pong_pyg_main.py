import pygame
pygame.init()
# Colors to be used for board and sphere
RED = (255, 0, 0)
WHITE = (255, 255, 255)

size = (800, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
# This will keep the game loop running until the game is over
gameLoop = True
# Set to 60 later
clock = pygame.time.Clock()

def draw_dashed_line(surface, color, start_pos, end_pos, width = 2, length = 10):
    # for loop to draw small lines to form a bigger dashed line
    pygame.draw.line(surface, color, start_pos, end_pos, width)



while gameLoop:
    # user does something
        # if close
            # close

    # Draw necessary items
    screen.fill(RED)
    # Draw line here

    # update
    pygame.display.flip()
    # 60 FPS
    clock.tick(60)





pygame.quit()






