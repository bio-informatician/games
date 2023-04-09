'''
Copyright 2023 Bio-informatician
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
'''
import pygame

# Initialize Pygame
pygame.init()

# Set the screen size and title
screen_size = (430, 430)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("GO Board Game")

# Load the board image
image = pygame.image.load("board.png")

# Get the dimensions of the image
image_rect = image.get_rect()
image_width = image_rect.width
image_height = image_rect.height

# Calculate the x and y coordinates
x = (screen_size[0] - image_width) // 2
y = (screen_size[1] - image_height) // 2

# Set up the game loop
game_over = False
clock = pygame.time.Clock()

# Set up some game variables
player_turn = "black"
board_state = [[None for i in range(9)] for j in range(9)]

# Define a function to place a stone on the board
def place_stone(row, col, player):
    board_state[row][col] = player

def check_captures(color):
    captured_stones = []
    for row in range(9):
        for col in range(9):
            if board_state[row][col] == color:
                captured_stones += check_group_captures(row, col, color)
    for stone in captured_stones:
        board_state[stone[0]][stone[1]] = None

def check_group_captures(row, col, color):
    captured_stones = []
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_row, new_col = row + dx, col + dy
        if (new_row < 0 or new_row >= 9 or new_col < 0 or new_col >= 9):
            continue
        if board_state[new_row][new_col] is None:
            return []
        if board_state[new_row][new_col] == color:
            continue
        group, liberties = find_group(new_row, new_col, [])
        if liberties == 0:
            captured_stones += group
    return captured_stones


def find_group(row, col, visited):
    color = board_state[row][col]
    if (row, col) in visited:
        return [], 0
    visited.append((row, col))
    group = [(row, col)]
    liberties = 0
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        new_row, new_col = row + dx, col + dy
        if (new_row < 0 or new_row >= 9 or new_col < 0 or new_col >= 9):
            continue
        if (new_row, new_col) in visited:
            continue
        if board_state[new_row][new_col] is None:
            liberties += 1
        elif board_state[new_row][new_col] == color:
            sub_group, sub_liberties = find_group(new_row, new_col, visited)
            group += sub_group
            liberties += sub_liberties
    return group, liberties




# Define a function to end the game
def end_game():
    global game_over
    game_over = True

    
# Main game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_game()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if it's the player's turn
            if player_turn == "black":
                # Get the position of the mouse click
                mouse_pos = pygame.mouse.get_pos()

                # Convert the mouse position to the row and column of the board
                cell_size = screen_size[0] // 9
                col = mouse_pos[0] // cell_size
                row = mouse_pos[1] // cell_size

                # Check if the cell is empty
                if board_state[row][col] is None:
                    # Place a black stone on the board
                    place_stone(row, col, "black")

                    # Check for captures
                    check_captures(player_turn)


                    # Change the turn to the white player
                    player_turn = "white"

                
                
            else:
           
                # Get the position of the mouse click
                mouse_pos = pygame.mouse.get_pos()

                # Convert the mouse position to the row and column of the board
                cell_size = screen_size[0] // 9
                col = mouse_pos[0] // cell_size
                row = mouse_pos[1] // cell_size

                # Check if the cell is empty
                if board_state[row][col] is None:
                    # Place a white stone on the board
                    place_stone(row, col, "white")

                    # Check for captures
                    check_captures(player_turn)

                    # Change the turn to the black player
                    player_turn = "black"


    # Draw the board
    screen.blit(image, (x, y))

    # Draw the stones on the board
    for row in range(9):
        for col in range(9):
            if board_state[row][col] == "black":
                # Draw a black stone at (row, col)
                cell_size = screen_size[0] // 9
                stone_size = cell_size // 2
                stone_pos = (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2)
                pygame.draw.circle(screen, (0, 0, 0), stone_pos, stone_size)
            elif board_state[row][col] == "white":
                # Draw a white stone at (row, col)
                cell_size = screen_size[0] // 9
                stone_size = cell_size // 2
                stone_pos = (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2)
                pygame.draw.circle(screen, (255, 255, 255), stone_pos, stone_size)

    
    # Check for captures
    check_captures(player_turn)


    # Update the display
    pygame.display.flip()

    # Tick the clock
    clock.tick(60)

# Quit Pygame
pygame.quit()

