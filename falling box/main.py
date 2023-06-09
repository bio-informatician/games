'''
Copyright 2023 Bio-informatician

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
import pygame
import random

# initialize pygame
pygame.init()

# set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("My Game")

# set up colors
black = (0, 0, 0)
white = (255, 255, 255)

# set up player
player_size = 50
player_x = screen_width // 2 - player_size // 2
player_y = screen_height - player_size - 10
player_speed = 5

# set up enemy
enemy_size = 50
enemy_x = random.randint(0, screen_width - enemy_size)
enemy_y = 0
enemy_speed = 5

# set up font
font = pygame.font.SysFont(None, 30)

# set up score
score = 0

# game loop
game_over = False
clock = pygame.time.Clock()

while not game_over:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    # handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_size:
        player_x += player_speed

    # handle enemy movement
    enemy_y += enemy_speed
    if enemy_y > screen_height:
        enemy_x = random.randint(0, screen_width - enemy_size)
        enemy_y = 0
        score += 1
        enemy_speed += 1

    # handle collision
    if player_x < enemy_x + enemy_size and player_x + player_size > enemy_x and player_y < enemy_y + enemy_size and player_y + player_size > enemy_y:
        game_over = True

    # draw screen
    screen.fill(white)
    pygame.draw.rect(screen, black, (player_x, player_y, player_size, player_size))
    pygame.draw.rect(screen, black, (enemy_x, enemy_y, enemy_size, enemy_size))

    # update score
    score_text = font.render("Score: " + str(score), True, black)
    screen.blit(score_text, (10, 10))

    # update display
    pygame.display.update()

    # set up clock
    clock.tick(60)

# end game
pygame.quit()
quit()
