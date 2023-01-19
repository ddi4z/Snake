import pygame,sys
from pygame.math import Vector2
from SNAKE_class import SNAKE
from FOOD_class import FOOD

class MAIN:
    def __init__(self,option,cell_number,snake_color,food_number):
        self.snake = SNAKE([Vector2(3,10),Vector2(2,10),Vector2(1,10)],Vector2(1,0),snake_color[0])
        self.food_list = [FOOD(cell_number)]
        for num in range(food_number-1):
            self.food_list.append(FOOD(cell_number))
        
        if option==2:
            self.snake2 = SNAKE([Vector2(cell_number-4,10),Vector2(cell_number-3,10),Vector2(cell_number-2,10)],Vector2(-1,0),snake_color[1])


        
        
        
        

    
    def update(self,option,cell_number):
        self.snake.move_snake()
        self.check_collision(option,cell_number)
        self.check_fail(option,cell_number)
        if option==2:
            self.snake2.move_snake()
            

    def draw_elements(self,option,screen,cell_size,cell_number,fruit,game_font):
        self.draw_grass(screen,cell_size,cell_number)
        self.snake.draw_snake(screen,cell_size)
        self.draw_score(screen,cell_size,cell_number,fruit,game_font)
        if option==2:
            self.snake2.draw_snake(screen,cell_size)
        for each_food in self.food_list:
            each_food.draw_food(screen, cell_size,fruit)

    def check_collision(self,option,cell_number):
        for each_food in self.food_list:
            if each_food.pos==self.snake.body[0]:
                each_food.randomize(cell_number)
                self.snake.add_block()
                self.snake.play_crunch_sound()
                if option==2:
                    self.snake2.add_block()

        for block in self.snake.body[1:]:
            for each_food in self.food_list:
                if block == each_food.pos:
                    each_food.randomize(cell_number)

        if option==2:
            for each_food in self.food_list:
                if each_food.pos==self.snake2.body[0]:
                    each_food.randomize(cell_number)
                    self.snake.add_block()
                    self.snake2.add_block()
                    self.snake2.play_crunch_sound()
                    for block in self.snake2.body[1:]:
                        if block == each_food.pos:
                            each_food.randomize(cell_number)
        

    def check_fail(self,option,cell_number):
        if not 0 <= self.snake.body[0].x < cell_number or not 0 <= self.snake.body[0].y < cell_number:
            self.game_over()

        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()



        if option==2:
            if not 0 <= self.snake2.body[0].x < cell_number or not 0 <= self.snake2.body[0].y < cell_number:
                self.game_over()

            for block in self.snake2.body[1:]:
                if block == self.snake2.body[0]:
                    self.game_over()
                if block == self.snake.body[0]:
                    self.game_over()

            for block in self.snake.body[1:]:
                if block == self.snake2.body[0]:
                    self.game_over()
            if (self.snake2.body[0].x==self.snake.body[0].x-1 or self.snake2.body[0].x==self.snake.body[0].x+1) and self.snake2.body[0].y==self.snake.body[0].y:
                self.game_over()
            if (self.snake2.body[0].y==self.snake.body[0].y-1 or self.snake2.body[0].y+1==self.snake.body[0].y+1) and self.snake2.body[0].x==self.snake.body[0].x:
                self.game_over()

    def game_over(self):
        sys.exit()

    def draw_grass(self,screen,cell_size,cell_number):
        grass_color = (167,209,61)
        for row in range (cell_number):
            if row % 2 ==0:
                for col in range(cell_number):
                    if col%2 ==0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)
            else:
                for col in range(cell_number):
                    if col%2 !=0:
                        grass_rect = pygame.Rect(col * cell_size, row * cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,grass_color,grass_rect)

    def draw_score(self,screen,cell_size,cell_number,fruit,game_font):
        score_text = str(len(self.snake.body) - 3)
        score_surface = game_font.render(score_text,True,(56,74,12))
        score_x = int(cell_size* cell_number - 60)
        score_y = int(cell_size* cell_number - 40)
        score_rect = score_surface.get_rect(center = (score_x,score_y))
        fruit_rect= fruit.get_rect(midright = (score_rect.left,score_rect.centery))
        bg_rect = pygame.Rect(fruit_rect.left,fruit_rect.top,fruit_rect.width + score_rect.width + 10,fruit_rect.height)
        
        pygame.draw.rect(screen,(167,209,61),bg_rect)
        pygame.draw.rect(screen,(56,74,12),bg_rect,2)
        screen.blit(score_surface,score_rect)
        screen.blit(fruit,fruit_rect)
