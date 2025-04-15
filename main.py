import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shots import *

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()
    
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)


    field = AsteroidField()
    gamer = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    dt = 0
   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatable.update(dt)
        screen.fill("black")
        
        for thing in drawable:
            thing.draw(screen)
            
        for ast in asteroids:
            for shot in shots:
                if ast.coll(shot):
                    ast.split()
                    shot.kill()
            if gamer.coll(ast):
                print("Game over")
                return
            
        
        dt = time.tick(60) / 1000
        
            
        pygame.display.flip()
    


if __name__ == "__main__":
    main()