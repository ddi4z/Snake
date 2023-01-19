import pygame,sys,random
from pygame.math import Vector2

class FOOD:
    def __init__(self,cell_number) -> None:
        self.randomize(cell_number)

    def draw_food(self,screen, cell_size,fruit):
        fruit_rect = pygame.Rect(int(self.pos.x * cell_size),int(self.pos.y * cell_size),cell_size,cell_size)
        screen.blit(fruit,fruit_rect)
    
    def randomize(self,cell_number):
        self.x = random.randint(0,cell_number -1)
        self.y = random.randint(0,cell_number -1)
        self.pos = Vector2(self.x,self.y)