import pygame,sys
from game import Game
from blocks import *
from colors import Colors

pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)

screen = pygame.display.set_mode((500, 620)) # Width, Height
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()
running = True

game = Game()
# Custom event - This will trigger every time the block position needs to be updated.
game_update = pygame.USEREVENT
pygame.time.set_timer(game_update, 200) # Updates the position of the block every 200 seconds.

# Game loop
while running:
    for event in pygame.event.get():
        # pygame.QUIT event allows the user to click X to close the game window.
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit 
        if event.type == pygame.KEYDOWN:
            if game.game_over == True:
                game.game_over = False
                game.reset()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
            if event.key == pygame.K_ESCAPE and game.game_over == False:
                game.paused()
        if event.type == game_update and game.game_over == False: 
            # This will continously bring the piece down 
            # whilst using the custom event outside the while loop
            game.move_down()
            
    # Game Rendering/Drawing
    screen.fill(Colors.dark_blue)
    game.draw(screen)
    
    pygame.display.update()
    clock.tick(60) # Limits the game to run at 60 FPS.
