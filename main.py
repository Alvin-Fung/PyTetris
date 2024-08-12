import pygame
from game import Game
from blocks import *
from colors import Colors
from controls import Controls

pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("Game Over!", True, Colors.white)

score_rect = pygame.Rect(320, 50, 170, 60)
next_rect = pygame.Rect(320, 215, 170, 180)

screen = pygame.display.set_mode((500, 620)) # Width, Height
pygame.display.set_caption("Python Tetris")

clock = pygame.time.Clock()
running = True

game = Game()
controls = Controls(game)

# Custom event - This will trigger every time the block position needs to be updated.
game.game_update = pygame.USEREVENT
pygame.time.set_timer(game.game_update, 200) # Updates the position of the block every 200 seconds.

# Game loop
while running:
    # Controls & Event handling
    controls.handle_events()
            
    # Game Rendering/Drawing
    
    #Score is dynamic and is not a static text
    score_value_surface = title_font.render(str(game.score), True, Colors.white)
    
    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))
    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))
    
    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 10) # 0 and 10 to have rounded corners
    screen.blit(score_value_surface, score_value_surface.get_rect(centerx = score_rect.centerx,
                centery = score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 10)
    game.draw(screen)
    
    pygame.display.update()
    clock.tick(60) # Limits the game to run at 60 FPS.
