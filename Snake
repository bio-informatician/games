import pygame
import random

def start_game():
    
    # Initialize Pygame
    pygame.init()

    # Set the dimensions of the game screen
    screen_width = 800
    screen_height = 600

    # Create the game screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Snake Game")

    # Set the font for displaying text
    font = pygame.font.SysFont("Arial", 30)

    # Set the colors for the game objects
    snake_color = (0, 255, 0)
    food_color = (255, 0, 0)

    # Set the starting position and size of the snake
    snake_size = 10
    snake_x = 250
    snake_y = 250
    snake_body = [(snake_x, snake_y)]

    # Set the starting position and size of the food
    food_size = 10
    food_x = random.randint(0, screen_width - food_size)
    food_y = random.randint(0, screen_height - food_size)

    # Set the speed and direction of the snake
    snake_speed = 10
    snake_direction = "right"

    # Set the initial score
    score = 0

    # Main game loop
    while True:

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return(score)
                quit()

        # Check for key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and snake_direction != "right":
            snake_direction = "left"
        elif keys[pygame.K_RIGHT] and snake_direction != "left":
            snake_direction = "right"
        elif keys[pygame.K_UP] and snake_direction != "down":
            snake_direction = "up"
        elif keys[pygame.K_DOWN] and snake_direction != "up":
            snake_direction = "down"

        # Move the snake
        if snake_direction == "left":
            snake_x -= snake_speed
        elif snake_direction == "right":
            snake_x += snake_speed
        elif snake_direction == "up":
            snake_y -= snake_speed
        elif snake_direction == "down":
            snake_y += snake_speed

        # Check for collision with the food
        if snake_x < food_x + food_size and snake_x + snake_size > food_x and snake_y < food_y + food_size and snake_y + snake_size > food_y:
            food_x = random.randint(0, screen_width - food_size)
            food_y = random.randint(0, screen_height - food_size)
            snake_body.append((0, 0))
            score += 1

        # Check for collision with the walls
        if snake_x < 0 or snake_x + snake_size > screen_width or snake_y < 0 or snake_y + snake_size > screen_height:
            pygame.quit()
            return(score)
            quit()

        # Check for collision with the snake's body
        for i in range(1, len(snake_body)):
            if snake_x == snake_body[i][0] and snake_y == snake_body[i][1]:
                pygame.quit()
                return(score)
                quit()

        # Move the snake's body
        for i in range(len(snake_body) - 1, 0, -1):
            snake_body[i] = (snake_body[i-1][0], snake_body[i-1][1])
        snake_body[0] = (snake_x, snake_y)

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw the food
        pygame.draw.rect(screen, food_color, (food_x, food_y, food_size, food_size))

        # Draw the snake
        for i in range(len(snake_body)):
            pygame.draw.rect(screen, snake_color, (snake_body[i][0], snake_body[i][1], snake_size, snake_size))

        # Draw the score
        score_text = font.render("Score: " + str(score), True, (255, 255, 255))
        screen.blit(score_text, (10, 10))

        # Update the screen
        pygame.display.update()

        # Set the game speed
        pygame.time.Clock().tick(30)
        
def show_menu():
    # Initialize Pygame
    pygame.init()

    # Set the dimensions of the menu screen
    screen_width = 800
    screen_height = 600

    # Create the menu screen
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Snake Game Menu")

    # Set the font for displaying text
    font = pygame.font.SysFont("Arial", 30)

    # Set the colors for the menu objects
    text_color = (255, 255, 255)
    button_color = (0, 255, 0)
    hover_color = (0, 200, 0)

    # Set the size and position of the start button
    button_width = 200
    button_height = 50
    button_x = screen_width/2 - button_width/2
    button_y = screen_height/2 - button_height/2

    # Main menu loop
    while True:

        # Check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if button_x < mouse_x < button_x + button_width and button_y < mouse_y < button_y + button_height:
                    score = start_game()
                    print("Game over! Score: " + str(score))
                    pygame.quit()

        # Draw the background
        screen.fill((0, 0, 0))

        # Draw the start button
        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
        pygame.draw.rect(screen, button_color, button_rect)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if button_rect.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(screen, hover_color, button_rect)
        else:
            pygame.draw.rect(screen, button_color, button_rect)

        # Draw the text
        text = font.render("Start", True, text_color)
        text_x = button_x + button_width/2 - text.get_width()/2
        text_y = button_y + button_height/2 - text.get_height()/2
        screen.blit(text, (text_x, text_y))

        # Update the screen
        pygame.display.update()

        # Set the game speed
        pygame.time.Clock().tick(30)

while True:
    show_menu()
