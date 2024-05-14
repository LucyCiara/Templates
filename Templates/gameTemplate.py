# Dependency import.
import sys 
import pygame
import random

# Initiation.
pygame.init()

# Setting variables.
fps = 60
fpsClock = pygame.time.Clock()
 
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Ensuring no object is placed in the same place by making finite positions.
xPositions = [i*50 for i in range(WIDTH//50)]
yPositions = [i*50 for i in range(HEIGHT//50)]
positions = []
for xPos in xPositions:
    for yPos in yPositions:
        positions.append([xPos, yPos])

# Superclass with traits for all objects.
class Entity:
    # Initiation for all objects.
    def __init__(self):
        coordinates = positions.pop(random.randint(0, len(positions)-1))
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.rect = pygame.Rect(self.x, self.y, 50, 50)

# Player class for a player object.
class Player(Entity):
    # Player specific initiation.
    def __init__(self):
        super().__init__()
        self.color = (255, 255, 255)

    # Movement of object.
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and keys[pygame.K_DOWN]:
            pass
        elif keys[pygame.K_UP] and pygame.Rect(self.x, self.y-1, 50, 50).collidelist(objects[2]) == -1:
            self.y -= 1
        elif keys[pygame.K_DOWN] and pygame.Rect(self.x, self.y+1, 50, 50).collidelist(objects[2]) == -1:
            self.y += 1
        if keys[pygame.K_LEFT] and keys[pygame.K_RIGHT]:
            pass
        elif keys[pygame.K_LEFT] and pygame.Rect(self.x-1, self.y, 50, 50).collidelist(objects[2]) == -1:
            self.x -= 1
        elif keys[pygame.K_RIGHT] and pygame.Rect(self.x+1, self.y, 50, 50).collidelist(objects[2]) == -1:
            self.x += 1
        self.rect = pygame.Rect(self.x, self.y, 50, 50)

    # Player specific updating.
    def update(self):
        self.movement()

# Obsticle class for non-moving, non-interactable objects.
class Obsticle(Entity):
    # Obsticle specific initiation.
    def __init__(self):
        super().__init__()
        self.color = (150, 150, 150)

    # Obsticle specific updating.
    def update(self):
        pass

# Enemy class for antagonistic or harmful objects.
class Enemy(Entity):
    # Enemy specific initiation.
    def __init__(self):
        super().__init__()
        self.color = (255, 0, 0)

    # Enemy specific updating.
    def update(self):
        self.collision()

    # Enemy specific collision detection and execution.
    def collision(self):
        global player
        if self.rect.colliderect(player.rect):
            pass

# Class for the resource to be collected.
class Resource(Entity):
    def __init__(self):
        super().__init__()
        self.color = (0, 255, 0)

    # Resource specific updating.
    def update(self):
        self.collision

    # Resource specific collision detection and execution.
    def collision(self):
        global player
        if self.rect.colliderect(player.rect):
            pass

# Creating objects.
player = Player()
objects = [[player], [Enemy() for i in range(2)], [Obsticle() for i in range(10)], [Resource() for i in range(3)]]
 
# Game loop.
run = True
while run:
    screen.fill((0, 0, 0))
    
    # Operation for quitting pygame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    # Update.
    for objectList in objects:
        for object in objectList:
            object.update()

    # Draw.
    for objectList in objects:
        for object in objectList:
            pygame.draw.rect(screen, object.color, object.rect) 

    pygame.display.flip()
    fpsClock.tick(fps)