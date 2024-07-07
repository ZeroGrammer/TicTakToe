
import pygame

class Mouse:
    
    def __init__(self):

        self.prev_left_button_state = False # False indicates not pressed
        pass

    def leftButtonReleased(self):
        
        mouse_button = pygame.mouse.get_pressed()
        is_left_button_released = False

        if self.prev_left_button_state and not mouse_button[0]:
            is_left_button_released = True

        self.prev_left_button_state = mouse_button[0]

        return is_left_button_released

    def getMouseCoords(self):

        coords = pygame.mouse.get_pos()
        return coords
