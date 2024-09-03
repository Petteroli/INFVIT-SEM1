import pygame as pg
import pygame.locals as local
import os
import math as mp
"test"
pg.init()

def pathRelToFolder(filePath):
    scriptDir = os.path.dirname(os.path.abspath(__file__))
    absFilePath = os.path.join(scriptDir, filePath)
    return absFilePath

clock = pg.time.Clock()
FPS = 60

width = 1000
height = 500
window = pg.display.set_mode((width, height))
bg_img = pg.image.load(pathRelToFolder("bakgrunn.jpeg"))
bg_img = pg.transform.scale(bg_img, (width, height))

image_sprite1 = [pg.image.load(pathRelToFolder("sprite1.png")),
                 pg.image.load(pathRelToFolder("sprite2.png"))]

obstacle_image = pg.image.load(pathRelToFolder("cactus.png"))
obstacle_image = pg.transform.scale(obstacle_image, (50, 120))

class Player():
    JUMP_HEIGHT = 230
    COLLISION_SHAPE = pg.Rect(0, 20, 64, 76)

    def __init__(self, x, y, speed,image):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = image
        self.rect = self.image.get_rect(x=x, y=y)
        self.is_jumping = False
        self.jump_height = 0
        self.start_y = y
        self.jump_duration = 60  
        self.jump_timer = 0
       
    def get_collision_rect(self):
        return self.COLLISION_SHAPE.move(self.x, self.y)   

    def move(self, buttons):
        if buttons[local.K_UP] and not self.is_jumping:
            self.is_jumping = True
            self.jump_timer = 0

        if self.is_jumping:
            self.jump_timer += 1
            jump_progress = self.jump_timer / self.jump_duration
            sine_wave = mp.sin(jump_progress * mp.pi)
            self.y = self.start_y - sine_wave * self.JUMP_HEIGHT

            if self.jump_timer >= self.jump_duration:
                self.is_jumping = False
                self.jump_timer = 0

        elif self.y < self.start_y:
            self.y += self.speed

            if self.y > self.start_y:
                self.y = self.start_y

    def draw(self, surface, value):
        if value >= len(image_sprite1):
            value = 0
        image = image_sprite1[value]
        x = self.x
        y = self.y
        surface.blit(image, (x, y))   

class Obstacle():
    def __init__(self, x, y, speed, image):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = image
        self.rect = self.image.get_rect(x=x, y=y)
        self.start_x = x
        self.score = 0

    def move(self):
        self.x -= self.speed
        self.rect.x = self.x
        if self.x + self.rect.width < 1:
            self.reset_position()
            self.score += 1

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def get_collision_rect(self):
        return self.rect.inflate(-20, -20)
    
    def collides_with(self, player):
        return self.get_collision_rect().colliderect(player.get_collision_rect())

    def reset_position(self):
        self.x = self.start_x


player = Player(80, 250, 5, image_sprite1[0])
obstacle = Obstacle(1000, 250, 5, obstacle_image)

i = 0
value = 0
animation_frame_count = 10 
animation_frame = 0
run = True
reset_delay = 60  
reset_timer = 0
score = 0
score_font = pg.font.SysFont(None, 30)

while run:
    for event in pg.event.get():
        if event.type == local.QUIT:
            run = False

    if player.get_collision_rect().colliderect(obstacle.get_collision_rect()):
        obstacle.reset_position()

    window.blit(bg_img, (i, 0))
    window.blit(bg_img, (width + i, 0))
    if i == -width:
        window.blit(bg_img, (width + i, 0))
        i = 0
    i -= 1


    player.move(pg.key.get_pressed())
    player.draw(window, animation_frame // animation_frame_count)
    animation_frame = (animation_frame + 1) % (animation_frame_count * len(image_sprite1))

    obstacle.move()
    obstacle.draw(window)
    if obstacle.x < 0:
        obstacle.reset_position()
        score += 1

    score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
    window.blit(score_text, (10, 10))

    if player.get_collision_rect().colliderect(obstacle.get_collision_rect()):
        run = False
        reset_timer = reset_delay

    if not run:
        reset_timer -= 1
        if reset_timer == 0:
            run = True
            player = Player(80, 250, 5, image_sprite1[0])
            obstacle = Obstacle(1000, 250, 5, obstacle_image)
            reset_timer = reset_delay


    pg.display.update()
    clock.tick(FPS)

pg.quit()