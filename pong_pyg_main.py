import pygame

from ball import Ball
from paddle import Paddle

pygame.init()
# Colors to be used for board and sphere
RED = (255, 0, 0)
WHITE = (255, 255, 255)

size = (800, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")
# create all the paddles and put them in their location( 3 per player)
paddleA1 = Paddle(WHITE, 10, 100)
paddleA1.rect.x = 20
paddleA1.rect.y = 200
paddleA2 = Paddle(WHITE, 10, 100)
paddleA2.rect.x = 20
paddleA2.rect.y = 100
paddleA3 = Paddle(WHITE, 10, 100)
paddleA3.rect.x = 20
paddleA3.rect.y = 400
paddleB1 = Paddle(WHITE, 10, 100)
paddleB1.rect.x = 770
paddleB1.rect.y = 200
paddleB2 = Paddle(WHITE, 10, 100)
paddleB2.rect.x = 770
paddleB2.rect.y = 100
paddleB3 = Paddle(WHITE, 10, 100)
paddleB3.rect.x = 770
paddleB3.rect.y = 400

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195
# This is so we can have all our obj in one obj to make it easier to draw later
sprites_list = pygame.sprite.Group()
sprites_list.add(paddleA1)
sprites_list.add(paddleA2)
sprites_list.add(paddleA3)
sprites_list.add(paddleB1)
sprites_list.add(paddleB2)
sprites_list.add(paddleB3)
sprites_list.add(ball)

# This will keep the game loop running until the game is over
gameLoop = True
# Set to 60 later
clock = pygame.time.Clock()
# Point and then game/ round score
scoreA = 0
scoreB = 0

game_countA = 0
game_countB = 0




def draw_dashed_line(surface, color, start_pos, end_pos, width = 2, length = 10):
    # for loop to draw small lines to form a bigger dashed line
    pygame.draw.line(surface, color, start_pos, end_pos, width)


while gameLoop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            gameLoop = False
    # Handle paddle movement with arrow keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        paddleB1.move_up(5)
    if keys[pygame.K_DOWN]:
        paddleB1.move_down(5)
    if keys[pygame.K_LEFT]:
        paddleB2.move_left(5)
        paddleB3.move_left(5)
    if keys[pygame.K_RIGHT]:
        paddleB2.move_left(5)
        paddleB3.move_left(5)

    sprites_list.update()

    # Check if ball hits a wall( 6 wall pieces to check and then reflect ball)
    if ball.rect.x >= 790:
        scoreA += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        scoreB += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y >= 490 and ball.rect.x <= 400:
        scoreB += 1
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y >= 490 and ball.rect.x >= 400:
        scoreA += 1
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y <= 0 and ball.rect.x <= 400:
        scoreB += 1
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y <= 0 and ball.rect.x >= 400:
        scoreA += 1
        ball.velocity[1] = -ball.velocity[1]

    # if ball hits a paddle
    if pygame.sprite.collide_mask(ball, paddleA1) or pygame.sprite.collide_mask(ball, paddleA2) or pygame.sprite.collide_mask(ball, paddleA3) or pygame.sprite.collide_mask(ball, paddleB1) or pygame.sprite.collide_mask(ball, paddleB2) or pygame.sprite.collide_mask(ball, paddleB3):
        ball.bounce()

    # Draw necessary items
    screen.fill(RED)
    # Draw line here(dashed line in next implementation)
    pygame.draw.line(screen, WHITE, [400,0], [400,500], 5)
    # Draw sprites
    sprites_list.draw(screen)
    # update scores
    font = pygame.font.Font(None, 76)
    text = font.render(str(scoreA), 1, WHITE)
    text2 = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (280,10))
    screen.blit(text2, (450, 10))

    # update
    pygame.display.flip()
    # 60 FPS
    clock.tick(60)





pygame.quit()






