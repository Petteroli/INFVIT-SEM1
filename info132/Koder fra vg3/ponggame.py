import pygame, random

# Initialize pygame
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Singleplayer Pong")

# Define colors
BLACK, WHITE = (0, 0, 0), (255, 255, 255)

# Define the game objects
class Game:
    def __init__(self):
        self.score, self.font = 0, pygame.font.SysFont("Monocraft", 30)
        
    def update(self):
        screen.blit(self.font.render(f"Score: {self.score}", True, WHITE), (10, 10))

class Ball:
    def __init__(self):
        self.x, self.y, self.size = random.randint(0, 780), 50, 20
        self.color, self.speed = WHITE, [random.randint(1, 2), random.randint(1, 2)]
        
    def update(self):
        self.x += self.speed[0]
        self.y += self.speed[1]
        if self.x <= 0: self.speed[0], self.x = -self.speed[0], 0
        elif self.x >= 780: self.speed[0], self.x = -self.speed[0], 780
        if self.y <= 0: self.speed[1], self.y = -self.speed[1], 0
        elif self.y >= 580: return True
        return False

class Paddle:
    def __init__(self):
        self.x, self.y, self.width, self.height = 350, 590, 100, 10
        self.color, self.speed = WHITE, 5
        
    def update(self):
        keys = pygame.key.get_pressed()
        self.x = max(0, min(700, self.x - keys[pygame.K_LEFT] * self.speed + keys[pygame.K_RIGHT] * self.speed))
        
    def hit_ball(self, ball):
        if (ball.y + ball.size >= self.y and ball.y + ball.size <= self.y + self.height) and (ball.x >= self.x and ball.x <= self.x + self.width):
            ball.speed[1], ball.y = -ball.speed[1], self.y - ball.size
            return True
        return False

# Create the game objects
game, balls, paddle = Game(), [Ball()], Paddle()

# Game loop
while True:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # Update the game objects
    game.update()
    paddle.update()
    
    for ball in balls[:]:
        if ball.update():
            balls.remove(ball)
            continue
        
        if paddle.hit_ball(ball):
            game.score += 1
    
    # Draw the game objects
    screen.fill(BLACK)
    
    for ball in balls:
        pygame.draw.rect(screen, ball.color, (ball.x, ball.y, ball.size, ball.size))
    
    pygame.draw.rect(screen, paddle.color, (paddle.x, paddle.y, paddle.width, paddle.height))
    
    pygame.display.flip()