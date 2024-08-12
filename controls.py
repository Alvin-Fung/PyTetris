import pygame

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
