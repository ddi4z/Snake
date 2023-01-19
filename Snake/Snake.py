import pygame,sys
from pygame.math import Vector2
from MAIN_class import MAIN
from BUTTON_class import BUTTON as Button


pygame.init()
cell_size = 40
cell_number = 21
snake_color = ["blue","red"]
option=1
food_number=1
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size ))
game_font = pygame.font.Font('Snake\Font\\PoetsenOne-Regular.ttf',25)
pygame.display.set_caption("Menu")
BG = pygame.image.load("Snake\Graphics\\menu\\Background.png")

def main_menu(option=1,food_number=1,snake_color=["blue","red"]):
    while True:
        screen.blit(BG, (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        text = game_font.render("SNAKE GAME", True, "white")
        rect = text.get_rect(center=((cell_size*cell_number)//2, 100))

        play_btn = Button(image=pygame.image.load("Snake\Graphics\\menu\\Play Rect.png"), pos=((cell_size*cell_number)//2, 250), 
                            text_input="PLAY", font=game_font, base_color="#d7fcd4", hovering_color="White")
        options_btn = Button(image=pygame.image.load("Snake\Graphics\\menu\\Options Rect.png"), pos=((cell_size*cell_number)//2, 400), 
                            text_input="OPTIONS", font=game_font, base_color="#d7fcd4", hovering_color="White")
        quit_btn = Button(image=pygame.image.load("Snake\Graphics\\menu\\Quit Rect.png"), pos=((cell_size*cell_number)//2, 550), 
                            text_input="QUIT", font=game_font, base_color="#d7fcd4", hovering_color="White")

        screen.blit(text, rect)

        for button in [play_btn, options_btn, quit_btn]:
            button.changeColor(mouse_pos)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_btn.checkForInput(mouse_pos):
                    play(option,food_number,snake_color)
                if options_btn.checkForInput(mouse_pos):
                    options()
                if quit_btn.checkForInput(mouse_pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def play(option,food_number,snake_color):
    while True:
        
        pygame.mixer.pre_init(44100,-16,2,512)
        clock = pygame.time.Clock()
        fruit =  pygame.image.load("Snake\Graphics\\food\\apple.png").convert_alpha()
        main_game = MAIN(option,cell_number,snake_color,food_number)
        screen_UPDATE = pygame.USEREVENT
        pygame.time.set_timer(screen_UPDATE,150)
        game_screen(option,clock,main_game,fruit,game_font,screen_UPDATE)


def game_screen(option,clock,main_game,fruit,game_font,screen_UPDATE):

    if option==1:
        while True:
            for event in pygame.event.get():
                if event.type == screen_UPDATE:
                    main_game.update(option,cell_number)
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
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            screen.fill((175,215,70))
            main_game.draw_elements(option,screen,cell_size,cell_number,fruit,game_font)
            pygame.display.update()
            clock.tick(60)
    if option!=1:
        while True:
            for event in pygame.event.get():
                if event.type == screen_UPDATE:
                    main_game.update(option,cell_number)
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
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            screen.fill((175,215,70))
            main_game.draw_elements(option,screen,cell_size,cell_number,fruit,game_font)
            pygame.display.update()
            clock.tick(60)
    
def options():
    while True:
        mouse_pos= pygame.mouse.get_pos()

        screen.fill((76, 192, 249))

        text = game_font.render("OPTIONS", True, "Black")
        rect= text.get_rect(center=((cell_size*cell_number)//2,100))
        screen.blit(text, rect)

        return_options = Button(image=None, pos=((cell_size*cell_number)//2, 700), text_input="BACK", font=game_font, base_color="Black", hovering_color="Green")


        return_options.changeColor(mouse_pos)
        return_options.update(screen)



        # Colors
        text_colors = game_font.render("Color", True, "Black")
        rect_colors= text.get_rect(center=(((cell_size*cell_number)//2)+20,150))
        screen.blit(text_colors, rect_colors)
        colors = {"blue":"orange","light_blue":"red","purple":"green","pink":"green","red":"light_blue","orange":"purple","yellow":"blue","green":"pink","black":"white","white":"black"}
        colors_btn = []
        x=75
        for color in colors:
            colors_btn.append((Button(image=pygame.image.load(f"Snake\Graphics\\{color}\\head_up.png"), pos=(x, 200), text_input="", font=game_font, base_color="#d7fcd4", hovering_color="White"),color))
            x+=75
        for btn in colors_btn:
            btn[0].update(screen)

        # Game mode
        text_snake = game_font.render("Game mode", True, "Black")
        rect_snake= text.get_rect(center=(((cell_size*cell_number)//2)-10,300))
        screen.blit(text_snake, rect_snake)
        option_one=Button(image=None, pos=(320, 350), text_input="1", font=game_font, base_color="black", hovering_color="White")
        option_two=Button(image=None, pos=(520, 350), text_input="2", font=game_font, base_color="black", hovering_color="White")
        option_one.changeColor(mouse_pos)
        option_one.update(screen)
        option_two.changeColor(mouse_pos)
        option_two.update(screen)

        # Food
        text_food = game_font.render("Fruits", True, "Black")
        rect_food= text.get_rect(center=(((cell_size*cell_number)//2)+20,400))
        screen.blit(text_food, rect_food)

        one_btn=Button(image=None, pos=(220, 450), text_input="1", font=game_font, base_color="black", hovering_color="White")
        three_btn=Button(image=None, pos=(420, 450), text_input="3", font=game_font, base_color="black", hovering_color="White")
        five_btn=Button(image=None, pos=(620, 450), text_input="5", font=game_font, base_color="black", hovering_color="White")
        one_btn.changeColor(mouse_pos)
        one_btn.update(screen)
        three_btn.changeColor(mouse_pos)
        three_btn.update(screen)
        five_btn.changeColor(mouse_pos)
        five_btn.update(screen)



                    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                for btn in colors_btn:
                    if btn[0].checkForInput(mouse_pos):
                        snake_color=[btn[1],colors[btn[1]]]
                        
                if option_one.checkForInput(mouse_pos):
                    option=1
                
                if option_two.checkForInput(mouse_pos):
                    option=2 

                if one_btn.checkForInput(mouse_pos):
                    food_number=1

                if three_btn.checkForInput(mouse_pos):
                    food_number=3

                if five_btn.checkForInput(mouse_pos):
                    food_number=5
                
                if return_options.checkForInput(mouse_pos):
                    main_menu(option,food_number,snake_color)

                
                

        pygame.display.update()

main_menu()