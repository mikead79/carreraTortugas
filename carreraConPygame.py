import pygame, sys
import random

class Runner():
    __customs = ("turtle", "fish", "prawn", "moray", "octopus")
    def __init__(self, x = 0, y = 0, custom = 0):
        self.custom = pygame.image.load("images/{}.png".format(self.__customs[custom]))
        self.position = [x, y]
        self.name = self.__customs[custom]
    
    def avanzar(self):
        self.position[0] += random.randint(1, 6)

class Game():
    __posY = [160, 200, 240, 280]
    __names = ("Speedy", "Lucera", "Alonso", "Torcuata")
    runners = []
    __startLine = 5
    __finishLine = 620
    
    def __init__(self):
        self.__screen = pygame.display.set_mode((640, 480))
        self.__background = pygame.image.load("images/background.png")
        pygame.display.set_caption("Carrera de bichos")
        
        for i in range(4):
            corredor = Runner(self.__startLine,self.__posY[i], i)
            corredor.name = self.__names[i]
            self.runners.append(corredor)
    
    def close(self):
        pygame.quit()
        sys.exit()
        
    def competir(self):
        gameOver = False
        while not gameOver:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameOver = True
            
            for theRunner in self.runners:
                theRunner.avanzar()
                if theRunner.position[0] >= self.__finishLine:
                    print("{} ha ganado!".format(theRunner.name))
                    gameOver = True
            
            self.__screen.blit(self.__background, (0,0))
            for runner in self.runners:
                self.__screen.blit(runner.custom, runner.position)
                
            
            pygame.display.flip()
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()

if __name__ == "__main__":
    game = Game()
    pygame.init()
    game.competir()