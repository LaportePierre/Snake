import random
import pygame
import sys

def main():
    s = snake()

class snake:
    def __init__(self):
        self.score_win = 3072
        self.width = 640
        self.height = 480
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.length = 5
        self.positions = [(self.width // 2, self.height // 2 - i) for i in range(self.length)]        
        self.direction = (0, -1)
        self.is_key_pressed = False
        self.popup_message = None
        self.fruit_position = self.generate_fruit((0, 255, 0))
        self.game()

    def game(self):
        pygame.init()
        pygame.display.set_caption("Snake project")

        # Colors
        black = (0, 0, 0)
        white = (255, 255, 255)
        yellow = (255, 255, 0)
        red = (255, 0, 0)
        green = (0, 255, 0)

        # Coloring to black the past snake position
        for position in self.positions:
            pygame.draw.rect(self.screen, black, (position[0], position[1], 10, 10))

        clock = pygame.time.Clock()

        # Main loop of the game
        while True:
            # Make the snake able to move with keybinds
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and self.is_key_pressed is False:
                    if event.key == pygame.K_UP:
                        if(self.direction != (0, 1)):
                            self.direction = (0, -1)
                            self.is_key_pressed = True
                    elif event.key == pygame.K_DOWN:
                        if(self.direction != (0, -1)):
                            self.direction = (0, 1)
                            self.is_key_pressed = True
                    elif event.key == pygame.K_LEFT:
                        if(self.direction != (1, 0)):
                            self.direction = (-1, 0)
                            self.is_key_pressed = True
                    elif event.key == pygame.K_RIGHT:
                        if(self.direction != (-1, 0)):
                            self.direction = (1, 0)
                            self.is_key_pressed = True
                # Showing reset button
                elif event.type == pygame.MOUSEBUTTONDOWN and self.game_running is False:
                    if replay_button_rect.collidepoint(event.pos):
                        self.reset_game(black)

            if self.popup_message is None:
                # New head snake position
                head_position = (self.positions[0][0] + (self.direction[0] * 10), self.positions[0][1] + (self.direction[1] * 10))
                collect_fruit = False
                # Collisions
                if (head_position[0] < 0 or head_position[0] >= self.width or head_position[1] < 0 or head_position[1] >= self.height):
                    self.popup_message = "Game Over! You hit the wall. Your score is " + str(self.length - 5)
                    self.game_running = False
                elif (head_position[0] == self.fruit_position[0] and head_position[1] == self.fruit_position[1]):
                    collect_fruit = True
                    self.length = self.length + 1
                elif(self.length - 5 == self.score_win):
                    self.popup_message = "Vous avez gagné "
                    self.game_running = False
                else: 
                    for i in range(1, len(self.positions)):
                        if(self.positions[i] == head_position):
                            self.popup_message = "Game Over! You hit yourself. Your score is " + str(self.length - 5)
                            self.game_running = False

                # Draw the game (first part)
                if collect_fruit is False:
                    position = self.positions[len(self.positions) - 1]
                    pygame.draw.rect(self.screen, black, (position[0], position[1], 10, 10))

                # Make the snake advance
                if collect_fruit is False:
                    self.positions = [head_position] + self.positions[:-1]
                else:
                    self.positions = [head_position] + self.positions
                    self.fruit_position = self.generate_fruit(green)

                # Draw the game (second part (snake))
                for position in self.positions:
                    pygame.draw.rect(self.screen, white, (position[0], position[1], 10, 10))
                pygame.draw.rect(self.screen, yellow, (head_position[0], head_position[1], 10, 10))
                
                # Refresh the self.screen
                pygame.display.flip()

                self.is_key_pressed = False

                # Speed of the game
                clock.tick(10)
            else:
                # Showing popup
                color = red
                if(self.length - 5 == self.score_win):
                    color = green
                popup_font = pygame.font.Font(None, 36)
                popup_text = popup_font.render(self.popup_message, True, color)
                popup_rect = popup_text.get_rect(center=(self.width // 2, self.height // 2))
                self.screen.blit(popup_text, popup_rect.topleft)
                replay_button = pygame.font.Font(None, 30).render("Try again !", True, color)
                replay_button_rect = replay_button.get_rect(center=(self.width // 2, self.height // 2 + 50))
                self.screen.blit(replay_button, replay_button_rect.topleft)
                pygame.display.flip()

    def reset_game(self, black):
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.length = 5
        self.positions = [(self.width // 2, self.height // 2 - i) for i in range(self.length)]        
        self.direction = (0, -1)
        self.is_key_pressed = False
        self.popup_message = None
        self.fruit_position = self.generate_fruit((0, 255, 0))
        pygame.display.flip()

    def generate_fruit(self, green):
        # Génère une position aléatoire pour le fruit qui n'est pas sur le serpent
        while True:
            x = random.randrange(self.width)
            y = random.randrange(self.height)
            x = (x // 10) * 10
            y = (y // 10) * 10 
            if (x, y) not in self.positions:
                print(x, y)
                pygame.draw.rect(self.screen, green, (x, y, 10, 10))
                return x, y

main()