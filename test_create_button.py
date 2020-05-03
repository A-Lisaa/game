import pygame
import test_buttons
from pygame.locals import *

#Initialize pygame
pygame.init()

class Button_Example:
    def __init__(self):
        self.main()
    
    #Create a display
    def display(self):
        self.screen = pygame.display.set_mode((650,370),0,32)
        pygame.display.set_caption("Buttons.py - example")

    #Update the display and show the button
    def update_display(self):
        self.screen.fill((30,144,255))
        #Parameters:               surface,      color,       x,   y,   length, height, width,    text,      text_color
        self.Button1.create_button(self.screen, (107,142,35), 225, 135, 200,    100,    0,        "Example", (255,255,255))
        pygame.display.flip()


    #Run the loop
    def main(self):
        self.Button1 = test_buttons.Button()
        self.display()
        while True:
            self.update_display()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == MOUSEBUTTONDOWN:
                    if self.Button1.pressed(pygame.mouse.get_pos()):
                        print ("Give me a command!")

if __name__ == '__main__':
    obj = Button_Example()