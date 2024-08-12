import pygame,sys
import game

class Controls:
    def __init__(self, game):
        self.game = game
        
    def handle_keydown(self, event):
        if self.game.game_over:
            self.game.game_over = False
            self.game.reset()
        else:
            if event.key == pygame.K_a and self.game.game_over == False:
                self.game.move_left()
            elif event.key == pygame.K_d and self.game.game_over == False:
                self.game.move_right()
            elif event.key == pygame.K_w and self.game.game_over == False:
                self.game.rotate()
            elif event.key == pygame.K_s and self.game.game_over == False:
                self.game.move_down()
                self.game.update_score(0, 1)
            elif event.key == pygame.K_ESCAPE and self.game.game_over == False:
                self.game.paused()
    
    def handle_events(self):
        for event in pygame.event.get():
        # pygame.QUIT event allows the user to click X to close the game window.
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit 
            if event.type == pygame.KEYDOWN:
                self.handle_keydown(event)
            if event.type ==  self.game.game_update and self.game.game_over == False: 
                # This will continously bring the piece down 
                # whilst using the custom event outside the while loop
                self.game.move_down()
