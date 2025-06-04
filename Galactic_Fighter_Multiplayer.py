# NAME: Alfred Davis
# DATE: 4/9/2025
# PURPOSE: A spaceship game similar to "asteroids"

import pygame
import random

pygame.init() 
font = pygame.font.Font(None, 100)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
screen_width, screen_height = screen.get_size()
background_image = pygame.image.load('star_background.png')
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
clock = pygame.time.Clock()
class MySprite(pygame.sprite.Sprite):
    def __init__(self, image_path, x, y):
        super().__init__()
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
sprites = pygame.sprite.Group()

# INPUT: None
# RETURN: None
# PURPOSE: displays the title screen
def title_screen():
    help_screen = False
    title_screen = pygame.image.load("title_screen.png")
    title_screen = pygame.transform.scale(title_screen, (screen_width, screen_height))
    screen.blit(title_screen, (0, 0))
    while True:
        pygame.event.get()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            if help_screen == False:
                pygame.time.delay(500)
                return
            else:
                title_screen = pygame.transform.scale(title_screen, (screen_width, screen_height))
                screen.blit(title_screen, (0, 0))
                help_screen = False
                pygame.time.delay(500)
        if keys[pygame.K_h]:
            help_screen = pygame.image.load("help.png")
            help_screen = pygame.transform.scale(help_screen, (screen_width, screen_height))
            screen.blit(help_screen, (0, 0))
            help_screen = True
            pygame.time.delay(500)
        pygame.display.flip()
        clock.tick(60)

# INPUT: None
# RETURN: None
# PURPOSE: plays the game credits
def credits():
    credits_screen = pygame.image.load("credits_screen_1.png")
    credits_screen = pygame.transform.scale(credits_screen, (screen_width, screen_height))
    screen.blit(credits_screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(5000)
    credits_screen = pygame.image.load("credits_screen_2.png")
    credits_screen = pygame.transform.scale(credits_screen, (screen_width, screen_height))
    screen.blit(credits_screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(5000)
    credits_screen = pygame.image.load("credits_screen_3.png")
    credits_screen = pygame.transform.scale(credits_screen, (screen_width, screen_height))
    screen.blit(credits_screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(5000)
    credits_screen = pygame.image.load("credits_screen_4.png")
    credits_screen = pygame.transform.scale(credits_screen, (screen_width, screen_height))
    screen.blit(credits_screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(5000)
    credits_screen = pygame.image.load("credits_screen_5.png")
    credits_screen = pygame.transform.scale(credits_screen, (screen_width, screen_height))
    screen.blit(credits_screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(5000)
    credits_screen = pygame.image.load("credits_screen_6.png")
    credits_screen = pygame.transform.scale(credits_screen, (screen_width, screen_height))
    screen.blit(credits_screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(5000)


# INPUT: None
# RETURN: None
# PURPOSE: Shows the game over screen
def game_over_screen():
    game_over_screen = pygame.image.load("game_over.png")
    game_over_screen = pygame.transform.scale(game_over_screen, (screen_width, screen_height))
    screen.blit(game_over_screen, (0, 0))
    pygame.display.flip()
    pygame.time.delay(10000)

# INPUT: sprite
# RETURN: None
# PURPOSE: Houses the main game loop
def game_loop(sprites):
    # Defining all my variables
    blaster_sprite = MySprite("blaster_bolt.png", 0, 0)
    score = 0
    explosion = False
    explosion_time = 0
    fire = False
    running = True
    spaceship = "up"
    player_1_dict = {
        "up": "spaceship.png",
        "down": "spaceship_down.png",
        "left": "spaceship_left.png",
        "right": "spaceship_right.png"
    }
    player_2_dict = {
        "up": "enemy_ship_up.png",
        "down": "enemy_ship_down.png",
        "left": "enemy_ship_left.png",
        "right": "enemy_ship_right.png"
    }
    ship_1_sprite = MySprite(player_1_dict["right"], -70, 400)
    ship_1_sprite.rect = ship_1_sprite.image.get_rect(center = ship_1_sprite.rect.center)
    sprites.add(ship_1_sprite)
    ship_2_sprite = MySprite(player_2_dict["left"], screen_width -70, 400)
    ship_1_sprite.rect = ship_1_sprite.image.get_rect(center = ship_1_sprite.rect.center)
    sprites.add(ship_2_sprite)
    while running:
        pygame.event.get()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and ship_1_sprite.rect.x >= 0:
            ship_1_sprite.rect.y -= 5
            ship_1_sprite.image = pygame.image.load(player_1_dict["up"]).convert_alpha()
            ship_1_sprite.rect = ship_1_sprite.image.get_rect(center = ship_1_sprite.rect.center)
            spaceship = "up"
        if keys[pygame.K_DOWN]:
            ship_1_sprite.rect.y += 5
            ship_1_sprite.image = pygame.image.load(player_1_dict["down"]).convert_alpha()
            ship_1_sprite.rect = ship_1_sprite.image.get_rect(center = ship_1_sprite.rect.center)
            spaceship = "down"
        if keys[pygame.K_LEFT]:
            ship_1_sprite.rect.x -= 5
            ship_1_sprite.image = pygame.image.load(player_1_dict["left"]).convert_alpha()
            ship_1_sprite.rect = ship_1_sprite.image.get_rect(center = ship_1_sprite.rect.center)
            spaceship = "left"
        if keys[pygame.K_RIGHT]:
            ship_1_sprite.rect.x += 5
            ship_1_sprite.image = pygame.image.load(player_1_dict["right"]).convert_alpha()
            ship_1_sprite.rect = ship_1_sprite.image.get_rect(center = ship_1_sprite.rect.center)
            spaceship = "right"
        if ship_1_sprite.rect.x < 0:
            ship_1_sprite.rect.x = 0
        if ship_1_sprite.rect.x > screen_width - 108:
            ship_1_sprite.rect.x = screen_width - 108
        if ship_1_sprite.rect.y < 0:
            ship_1_sprite.rect.y = 0
        if ship_1_sprite.rect.y > screen_height - 152:
            ship_1_sprite.rect.y = screen_height - 152
        if keys[pygame.K_ESCAPE]:
            running = False
        if fire == True:
            if fire_direction == "up":
                blaster_sprite.rect.y -= 10
            elif fire_direction == "down":
                blaster_sprite.rect.y += 10
            elif fire_direction == "left":
                blaster_sprite.rect.x -= 10
            elif fire_direction == "right":
                blaster_sprite.rect.x += 10
            if blaster_sprite.rect.y <= -21 or blaster_sprite.rect.x <= -21:
                fire = False
            elif blaster_sprite.rect.y >= screen_height or blaster_sprite.rect.x >= screen_width:
                fire = False
        if keys[pygame.K_SPACE] and fire == False:
            if spaceship == "up":
                x = ship_1_sprite.rect.x + ship_1_sprite.rect.width // 2
                y = ship_1_sprite.rect.y
                fire_direction = "up"
                blaster_sprite = MySprite("blaster_bolt.png", x, y)
            elif spaceship == "down":
                x = ship_1_sprite.rect.x + ship_1_sprite.rect.width // 2
                y = ship_1_sprite.rect.y + 152
                fire_direction = "down"
                blaster_sprite = MySprite("blaster_bolt.png", x, y)
            elif spaceship == "left":
                x = ship_1_sprite.rect.x
                y = ship_1_sprite.rect.y + ship_1_sprite.rect.height // 2
                fire_direction = "left"
                blaster_sprite = MySprite("blaster_bolt_side.png", x, y)
            elif spaceship == "right":
                x = ship_1_sprite.rect.x + 152
                y = ship_1_sprite.rect.y + ship_1_sprite.rect.height // 2
                fire_direction = "right"
                blaster_sprite = MySprite("blaster_bolt_side.png", x, y)
            sprites.add(blaster_sprite)
            fire = True
        if explosion == True:
            if explosion_time == 0:
                explosion_sprite = MySprite("explosion.png", x, y)
                sprites.add(explosion_sprite)
            explosion_time += 1
            if explosion_time > 60:
                sprites.remove(explosion_sprite)
                explosion_time = 0
                explosion = False
        screen.blit(background_image, (0, 0))
        text = font.render(f"{score}", True, (0, 0, 0), (255, 255, 255))
        background_image.blit(text, (0, 0))
        sprites.draw(screen)
        pygame.display.flip()
        clock.tick(60)

# INPUT: None
# RETURN: None
# PURPOSE: runs the program
def main():
    title_screen()
    won_or_lost = game_loop(sprites)
    if won_or_lost == True:
        credits()
    if won_or_lost == False:
        game_over_screen()

main()
pygame.quit()