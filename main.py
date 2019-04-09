import turtle

class Circuito():
    corredores = []
    __colorTurtle = ('red', 'black', 'blue', 'green')
    def __init__(self, width, height):
        self.__screen = turtle.Screen()
        self.__screen.setup(width, height)
        self.__screen.bgcolor('lightgray')
        
        self.__startLine = -width/2 + 20
        self.__finishLine = width/2 - 20
        
        for i in range(4):
            new_turtle = turtle.Turtle()
            new_turtle.shape('turtle')
            new_turtle.color(self.__colorTurtle[i])
            new_turtle.penup()
            new_turtle.setpos(self.__startLine, -45 + i * 30)
            self.corredores.append(new_turtle)
    
    def competir(self):
        pass

if __name__ == "__main__":
    circuito = Circuito(640, 480)
        