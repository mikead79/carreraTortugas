import pygame, sys

class Runner():
    def __init__(self, x = 0, y = 0):
        
        self.custom = pygame.image.load("images/fish.png")
        self.position = [x, y]
        self.name = "Speedy"
    
class Game():
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        self.__background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera de bichos")
        
        self.runner = Runner(320, 240)
    
    def start(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        # Mover hacia arriba runner
                        self.runner.position[1] -= 5
                    elif event.key == pygame.K_DOWN:
                        # Mover hacia abajo runner
                        self.runner.position[1] += 5
                    elif event.key == pygame.K_LEFT:
                        # Mover hacia izquierda runner
                        self.runner.position[0] -= 5
                    elif event.key == pygame.K_RIGHT:
                        # Mover hacia derecha runner
                        self.runner.position[0] += 5
                    else:
                        pass
            self.__screen.blit(self.__background, (0,0))
            self.__screen.blit(self.runner.custom, self.runner.position)
            pygame.display.flip()
                    
if __name__ == "__main__":
    game = Game()
    pygame.init()
    game.start()

