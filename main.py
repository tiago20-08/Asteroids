import pygame
from constants import *
from player import Player
from circleshape import *
from asteroid import *



def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    gamer = Player(x, y, PLAYER_RADIUS)
    

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0.03

    while True:
        screen.fill("black")

        for sprite in drawable:
            pygame.draw.polygon(screen, "white", sprite.triangle(), 2)
            pygame.draw.circle(screen, "white", sprite.circle(), 2)
        
        updatable.update(dt)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.display.flip()
        
        time.tick(60)




if __name__ == "__main__":
    main()