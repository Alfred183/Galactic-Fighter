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
ship_sprite = MySprite("spaceship.png", 800, 500)
ship_sprite.rect = ship_sprite.image.get_rect(center = ship_sprite.rect.center)
sprites = pygame.sprite.Group(ship_sprite)

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
    won = False
    blaster_sprite = MySprite("blaster_bolt.png", 0, 0)
    type = 0
    score = 0
    boss = False
    explosion = False
    wave_running = False
    explosion_time = 0
    enemy_1_iterate = 0
    enemy_2_iterate = 0
    enemy_3_iterate = 0
    enemy_4_iterate = 0
    boss_iterate = 0
    enemy_1 = False
    enemy_2 = False
    enemy_3 = False
    enemy_4 = False
    fire = False
    running = True
    spaceship = "up"
    enemy_dict = {
        "up": "enemy_ship_up.png",
        "down": "enemy_ship_down.png",
        "left": "enemy_ship_left.png",
        "right": "enemy_ship_right.png"
    }
    won = False
    while running:
        pygame.event.get()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and ship_sprite.rect.x >= 0:
            ship_sprite.rect.y -= 5
            ship_sprite.image = pygame.image.load("spaceship.png").convert_alpha()
            ship_sprite.rect = ship_sprite.image.get_rect(center = ship_sprite.rect.center)
            spaceship = "up"
        if keys[pygame.K_DOWN]:
            ship_sprite.rect.y += 5
            ship_sprite.image = pygame.image.load("spaceship_down.png").convert_alpha()
            ship_sprite.rect = ship_sprite.image.get_rect(center = ship_sprite.rect.center)
            spaceship = "down"
        if keys[pygame.K_LEFT]:
            ship_sprite.rect.x -= 5
            ship_sprite.image = pygame.image.load("spaceship_left.png").convert_alpha()
            ship_sprite.rect = ship_sprite.image.get_rect(center = ship_sprite.rect.center)
            spaceship = "left"
        if keys[pygame.K_RIGHT]:
            ship_sprite.rect.x += 5
            ship_sprite.image = pygame.image.load("spaceship_right.png").convert_alpha()
            ship_sprite.rect = ship_sprite.image.get_rect(center = ship_sprite.rect.center)
            spaceship = "right"
        if ship_sprite.rect.x < 0:
            ship_sprite.rect.x = 0
        if ship_sprite.rect.x > screen_width - 108:
            ship_sprite.rect.x = screen_width - 108
        if ship_sprite.rect.y < 0:
            ship_sprite.rect.y = 0
        if ship_sprite.rect.y > screen_height - 152:
            ship_sprite.rect.y = screen_height - 152
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
                x = ship_sprite.rect.x + ship_sprite.rect.width // 2
                y = ship_sprite.rect.y
                fire_direction = "up"
                blaster_sprite = MySprite("blaster_bolt.png", x, y)
            elif spaceship == "down":
                x = ship_sprite.rect.x + ship_sprite.rect.width // 2
                y = ship_sprite.rect.y + 152
                fire_direction = "down"
                blaster_sprite = MySprite("blaster_bolt.png", x, y)
            elif spaceship == "left":
                x = ship_sprite.rect.x
                y = ship_sprite.rect.y + ship_sprite.rect.height // 2
                fire_direction = "left"
                blaster_sprite = MySprite("blaster_bolt_side.png", x, y)
            elif spaceship == "right":
                x = ship_sprite.rect.x + 152
                y = ship_sprite.rect.y + ship_sprite.rect.height // 2
                fire_direction = "right"
                blaster_sprite = MySprite("blaster_bolt_side.png", x, y)
            sprites.add(blaster_sprite)
            fire = True
        if wave_running == False:
            type = random.randint(1, 4)
        if type == 1:
            if wave_running == False:
                enemy_ship_1 = MySprite(enemy_dict["left"], screen_width + 70, 400)
                sprites.add(enemy_ship_1)
                enemy_1 = True
                wave_running = True
            if enemy_1 == True:
                if enemy_1_iterate <= 60:
                    enemy_1_iterate += 1
                elif enemy_1_iterate > 60 and enemy_1_iterate <= 120:
                    enemy_ship_1.rect.x -= 5
                    enemy_1_iterate += 1
                elif enemy_1_iterate > 120 and enemy_1_iterate <= 180:
                    enemy_ship_1.image = pygame.image.load(enemy_dict["up"])
                    enemy_ship_1.rect.y -= 5
                    enemy_1_iterate += 1
                elif enemy_1_iterate > 180 and enemy_1_iterate <= 420:
                    enemy_ship_1.image = pygame.image.load(enemy_dict["left"])
                    enemy_ship_1.rect.x -= 5
                    enemy_1_iterate += 1
                elif enemy_1_iterate > 420 and enemy_1_iterate <= 540:
                    enemy_ship_1.image = pygame.image.load(enemy_dict["down"])
                    enemy_ship_1.rect.y += 5
                    enemy_1_iterate += 1
                elif enemy_1_iterate > 540 and enemy_1_iterate <= 780:
                    enemy_ship_1.image = pygame.image.load(enemy_dict["right"])
                    enemy_ship_1.rect.x += 5
                    enemy_1_iterate += 1
                elif enemy_1_iterate > 780 and enemy_1_iterate <= 840:
                    enemy_ship_1.image = pygame.image.load(enemy_dict["up"])
                    enemy_ship_1.rect.y -= 5
                    enemy_1_iterate += 1
                else:
                    enemy_1_iterate = 121
                if pygame.sprite.collide_rect(blaster_sprite, enemy_ship_1):
                    enemy_1_iterate = 0
                    x, y = (enemy_ship_1.rect.x, enemy_ship_1.rect.y)
                    sprites.remove(blaster_sprite)
                    sprites.remove(enemy_ship_1)
                    explosion = True
                    enemy_1 = False
                    score += 10
                    wave_running = False
                if pygame.sprite.collide_rect(ship_sprite, enemy_ship_1):
                    enemy_1_iterate = 0
                    x, y = (ship_sprite.rect.x, ship_sprite.rect.y)
                    sprites.remove(enemy_ship_1)
                    sprites.remove(ship_sprite)
                    enemy_1 = False
                    won_or_lost = False
                    explosion_sprite = MySprite("big_explosion.png", x, y)
                    sprites.add(explosion_sprite)
                    sprites.draw(screen)
                    pygame.display.flip()
                    pygame.time.delay(1000)
                    return won_or_lost
        if type == 2:
            if wave_running == False:
                if enemy_2 == False:
                    enemy_ship_2 = MySprite(enemy_dict["down"], screen_width // 2, -70)
                    sprites.add(enemy_ship_2)
                    enemy_2 = True
                    wave_running = True
            if enemy_2 == True:
                if enemy_2_iterate <= 120:
                    enemy_2_iterate += 1
                elif enemy_2_iterate > 120 and enemy_2_iterate <= 180:
                    enemy_ship_2.rect.y += 5
                    enemy_2_iterate += 1
                elif enemy_2_iterate > 180:
                    if ship_sprite.rect.y > enemy_ship_2.rect.y:
                        enemy_ship_2.rect.y += 2
                        enemy_ship_2.image = pygame.image.load(enemy_dict["down"])
                    if ship_sprite.rect.y < enemy_ship_2.rect.y:
                        enemy_ship_2.rect.y -= 2
                        enemy_ship_2.image = pygame.image.load(enemy_dict["up"])
                    if ship_sprite.rect.x > enemy_ship_2.rect.x:
                        enemy_ship_2.rect.x += 2
                        enemy_ship_2.image = pygame.image.load(enemy_dict["right"])
                    if ship_sprite.rect.x < enemy_ship_2.rect.x:
                        enemy_ship_2.rect.x -= 2
                        enemy_ship_2.image = pygame.image.load(enemy_dict["left"])
                if pygame.sprite.collide_rect(blaster_sprite, enemy_ship_2):
                    enemy_2_iterate = 0
                    x, y = (enemy_ship_2.rect.x, enemy_ship_2.rect.y)
                    sprites.remove(blaster_sprite)
                    sprites.remove(enemy_ship_2)
                    explosion = True
                    enemy_2 = False
                    score += 10
                    wave_running = False
                if pygame.sprite.collide_rect(ship_sprite, enemy_ship_2):
                    enemy_2_iterate = 0
                    x, y = (ship_sprite.rect.x, ship_sprite.rect.y)
                    sprites.remove(enemy_ship_2)
                    sprites.remove(ship_sprite)
                    enemy_2 = False
                    won_or_lost = False
                    explosion_sprite = MySprite("big_explosion.png", x, y)
                    sprites.add(explosion_sprite)
                    sprites.draw(screen)
                    pygame.display.flip()
                    pygame.time.delay(1000)
                    return won_or_lost
        if type == 3:
            if wave_running == False:
                enemy_ship_3 = MySprite(enemy_dict["right"], -70, 400)
                sprites.add(enemy_ship_3)
                enemy_3 = True
                wave_running = True
            if enemy_3 == True:
                if enemy_3_iterate <= 60:
                    enemy_3_iterate += 1
                elif enemy_3_iterate > 60 and enemy_3_iterate <= 120:
                    enemy_ship_3.rect.x += 5
                    enemy_3_iterate += 1
                elif enemy_3_iterate > 120 and enemy_3_iterate <= 180:
                    enemy_ship_3.image = pygame.image.load(enemy_dict["down"])
                    enemy_ship_3.rect.y += 5
                    enemy_3_iterate += 1
                elif enemy_3_iterate > 180 and enemy_3_iterate <= 420:
                    enemy_ship_3.image = pygame.image.load(enemy_dict["right"])
                    enemy_ship_3.rect.x += 5
                    enemy_3_iterate += 1
                elif enemy_3_iterate > 420 and enemy_3_iterate <= 540:
                    enemy_ship_3.image = pygame.image.load(enemy_dict["up"])
                    enemy_ship_3.rect.y -= 5
                    enemy_3_iterate += 1
                elif enemy_3_iterate > 540 and enemy_3_iterate <= 780:
                    enemy_ship_3.image = pygame.image.load(enemy_dict["left"])
                    enemy_ship_3.rect.x -= 5
                    enemy_3_iterate += 1
                elif enemy_3_iterate > 780 and enemy_3_iterate <= 840:
                    enemy_ship_3.image = pygame.image.load(enemy_dict["down"])
                    enemy_ship_3.rect.y += 5
                    enemy_3_iterate += 1
                else:
                    enemy_3_iterate = 121
                if pygame.sprite.collide_rect(blaster_sprite, enemy_ship_3):
                    enemy_3_iterate = 0
                    x, y = (enemy_ship_3.rect.x, enemy_ship_3.rect.y)
                    sprites.remove(blaster_sprite)
                    sprites.remove(enemy_ship_3)
                    explosion = True
                    enemy_3 = False
                    score += 10
                    wave_running = False
                if pygame.sprite.collide_rect(ship_sprite, enemy_ship_3):
                    enemy_3_iterate = 0
                    x, y = (ship_sprite.rect.x, ship_sprite.rect.y)
                    sprites.remove(enemy_ship_3)
                    sprites.remove(ship_sprite)
                    enemy_3 = False
                    won_or_lost = False
                    explosion_sprite = MySprite("big_explosion.png", x, y)
                    sprites.add(explosion_sprite)
                    sprites.draw(screen)
                    pygame.display.flip()
                    pygame.time.delay(1000)
                    return won_or_lost
        if type == 4:
            if wave_running == False:
                if enemy_4 == False:
                    enemy_ship_4 = MySprite(enemy_dict["up"], screen_width // 2, screen_height + 70)
                    sprites.add(enemy_ship_4)
                    enemy_4 = True
                    wave_running = True
            if enemy_4 == True:
                if enemy_4_iterate <= 120:
                    enemy_4_iterate += 1
                elif enemy_4_iterate > 120 and enemy_4_iterate <= 180:
                    enemy_ship_4.rect.y -= 5
                    enemy_4_iterate += 1
                elif enemy_4_iterate > 180:
                    if ship_sprite.rect.y > enemy_ship_4.rect.y:
                        enemy_ship_4.rect.y += 2
                        enemy_ship_4.image = pygame.image.load(enemy_dict["down"])
                    if ship_sprite.rect.y < enemy_ship_4.rect.y:
                        enemy_ship_4.rect.y -= 2
                        enemy_ship_4.image = pygame.image.load(enemy_dict["up"])
                    if ship_sprite.rect.x > enemy_ship_4.rect.x:
                        enemy_ship_4.rect.x += 2
                        enemy_ship_4.image = pygame.image.load(enemy_dict["right"])
                    if ship_sprite.rect.x < enemy_ship_4.rect.x:
                        enemy_ship_4.rect.x -= 2
                        enemy_ship_4.image = pygame.image.load(enemy_dict["left"])
                if pygame.sprite.collide_rect(blaster_sprite, enemy_ship_4):
                    enemy_4_iterate = 0
                    x, y = (enemy_ship_4.rect.x, enemy_ship_4.rect.y)
                    sprites.remove(blaster_sprite)
                    sprites.remove(enemy_ship_4)
                    explosion = True
                    enemy_4 = False
                    score += 10
                    wave_running = False
                if pygame.sprite.collide_rect(ship_sprite, enemy_ship_4):
                    enemy_2_iterate = 0
                    x, y = (ship_sprite.rect.x, ship_sprite.rect.y)
                    sprites.remove(enemy_ship_4)
                    sprites.remove(ship_sprite)
                    enemy_2 = False
                    won_or_lost = False
                    explosion_sprite = MySprite("big_explosion.png", x, y)
                    sprites.add(explosion_sprite)
                    sprites.draw(screen)
                    pygame.display.flip()
                    pygame.time.delay(1000)
                    return won_or_lost
        if score >= 150:
            if boss == False:
                wave_running = True
                boss_health = 150
                boss_sprite = MySprite("final_boss.png", -10, screen_height // 2)
                sprites.add(boss_sprite)
                boss = True
            elif boss_iterate <= 60:
                boss_sprite.rect.x += 5
                boss_iterate += 1
                boss_sprite.image = pygame.image.load("final_boss.png").convert_alpha()
            elif boss_iterate > 60 and boss_iterate <= 115:
                boss_sprite.rect.y += 5
                boss_iterate += 1
                boss_sprite.image = pygame.image.load("final_boss.png").convert_alpha()
            elif boss_iterate > 115 and boss_iterate <= 180:
                boss_sprite.rect.x += 15
                boss_iterate += 1
                boss_sprite.image = pygame.image.load("final_boss.png").convert_alpha()
            elif boss_iterate > 180 and boss_iterate <= 290:
                boss_sprite.rect.y -= 5
                boss_iterate += 1
                boss_sprite.image = pygame.image.load("final_boss.png").convert_alpha()
            elif boss_iterate > 290 and boss_iterate <= 355:
                boss_sprite.rect.x -= 15
                boss_iterate += 1
                boss_sprite.image = pygame.image.load("final_boss.png").convert_alpha()
            elif boss_iterate > 355 and boss_iterate <= 410:
                boss_sprite.rect.y += 5
                boss_iterate += 1
                boss_sprite.image = pygame.image.load("final_boss.png").convert_alpha()
            else:
                boss_iterate = 60
            if pygame.sprite.collide_rect(blaster_sprite, boss_sprite):
                sprites.remove(blaster_sprite)
                boss_health -= 1
                boss_sprite.image = pygame.image.load("injured_boss.png").convert_alpha()
            if pygame.sprite.collide_rect(ship_sprite, boss_sprite):
                    boss_iterate = 0
                    x, y = (ship_sprite.rect.x, ship_sprite.rect.y)
                    sprites.remove(boss_sprite)
                    sprites.remove(ship_sprite)
                    boss = False
                    won = False
                    explosion_sprite = MySprite("biggest_explosion.png", x, y)
                    sprites.add(explosion_sprite)
                    sprites.draw(screen)
                    pygame.display.flip()
                    pygame.time.delay(1000)
                    return won
            if boss_health == 0:
                x, y = (boss_sprite.rect.x, boss_sprite.rect.y)
                sprites.remove(boss_sprite)
                sprites.remove(blaster_sprite)
                won = True
                explosion_sprite = MySprite("big_explosion.png", x, y)
                sprites.add(explosion_sprite)
                sprites.draw(screen)
                pygame.display.flip()
                pygame.time.delay(3000)
        if won == True:
            return won
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