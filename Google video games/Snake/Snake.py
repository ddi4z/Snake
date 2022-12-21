import pygame,sys,random
from pygame.math import Vector2
from SNAKE_class import SNAKE
from FOOD_class import FOOD

class MAIN:
    def __init__(self):
        self.snake = SNAKE([Vector2(3,10),Vector2(2,10),Vector2(1,10)],Vector2(1,0))
        self.food = FOOD(cell_number)
        if option==2:
            self.snake2 = SNAKE([Vector2(cell_number-4,10),Vector2(cell_number-3,10),Vector2(cell_number-2,10)],Vector2(-1,0),"red")
    
    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        if option==2:
            self.snake2.move_snake()

    def draw_elements(self):
        self.draw_grass()
        self.food.draw_food(screen, cell_size,fruit)
        self.snake.draw_snake(screen,cell_size)
        self.draw_score()
        if option==2:
            self.snake2.draw_snake(screen,cell_size)

    def check_collision(self):
        if self.food.pos==self.snake.body[0]:
            self.food.randomize(cell_number)
            self.snake.add_block()
            self.snake.play_crunch_sound()
            if option==2:
                self.snake2.add_block()

        for block in self.snake.body[1:]:
            if block == self.food.pos:
                self.food.randomize(cell_number)

        if option==2:
            if self.food.pos==self.snake2.body[0]:
                self.food.randomize(cell_number)
                self.snake.add_block()
                self.snake2.add_block()
                self.snake2.play_crunch_sound()
                for block in self.snake2.body[1:]:
                    if block == self.food.pos:
                        self.food.randomize(cell_number)
        

    def check_fail(self):
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
        #self.snake.reset()

    def draw_grass(self):
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

    def draw_score(self):
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


def game_screen(option):

    if option==1:
        while True:
            for event in pygame.event.get():
                if event.type == SCREEN_UPDATE:
                    main_game.update()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if main_game.snake.direction.y !=1:
                            main_game.snake.direction = Vector2 (0,-1)

                    if event.key == pygame.K_DOWN:
                        if main_game.snake.direction.y !=-1:
                            main_game.snake.direction = Vector2 (0,1)

                    if event.key == pygame.K_LEFT:
                        if main_game.snake.direction.x !=1:
                            main_game.snake.direction = Vector2 (-1,0)

                    if event.key == pygame.K_RIGHT:
                        if main_game.snake.direction.x !=-1:
                            main_game.snake.direction = Vector2 (1,0)


            screen.fill((175,215,70))
            main_game.draw_elements()
            pygame.display.update()
            clock.tick(60)
    if option!=1:
        while True:
            for event in pygame.event.get():
                if event.type == SCREEN_UPDATE:
                    main_game.update()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if main_game.snake.direction.y !=1:
                            main_game.snake.direction = Vector2 (0,-1)
                            main_game.snake2.direction = Vector2 (0,1)
                    if event.key == pygame.K_DOWN:
                        if main_game.snake.direction.y !=-1:
                            main_game.snake.direction = Vector2 (0,1)
                            main_game.snake2.direction = Vector2 (0,-1)
                    if event.key == pygame.K_LEFT:
                        if main_game.snake.direction.x !=1:
                            main_game.snake.direction = Vector2 (-1,0)
                            main_game.snake2.direction = Vector2 (1,0)
                    if event.key == pygame.K_RIGHT:
                        if main_game.snake.direction.x !=-1:
                            main_game.snake.direction = Vector2 (1,0)
                            main_game.snake2.direction = Vector2 (-1,0)

            screen.fill((175,215,70))
            main_game.draw_elements()
            pygame.display.update()
            clock.tick(60)



option=1

pygame.mixer.pre_init(44100,-16,2,512)
pygame.init()
cell_size = 40
cell_number = 21
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size ))
clock = pygame.time.Clock()
main_game = MAIN()
fruit =  pygame.image.load("Snake\Graphics\\food\\apple.png").convert_alpha()
game_font = pygame.font.Font('Snake\Font\\PoetsenOne-Regular.ttf',25)
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)
game_screen(option)