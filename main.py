import time
import os
import curses
import threading


from Shape import Shape


class Main:
    width = 15
    height = 15
    screen = curses.initscr()
    fallenshapes = []
    playing = True
    # currentShape = Shape()


    def __init__(self):
        self.screen = curses.initscr()
        self.currentShape = Shape(self.screen)

    # Game board drawing
    # I would like to make a board class
    # but i try to make this program a
    # bit simple so i just draw the board
    # in the main class instead

    def drawGround(self):
        for x in range(self.width):
            self.screen.addstr(self.height,x,"#")

    def drawWalls(self):
        for y in range(self.height):
            self.screen.addstr(y,0,"#")

    def draw(self): #draw everyting
        self.drawGround()
        self.drawWalls()
        for shape in self.fallenshapes:
            shape.drawShape()
        self.currentShape.drawShape()


    def collide(self):
        for p in self.currentShape.points:
            if(p[1]+1 >= self.height):
                return True
            for shape in self.fallenshapes:
                for p1 in shape.points:
                    if(p[0]==p1[0] and p1[1]==p[1]+1):
                        return True

        return False

    def land():
        tempshape = self.currentShape.copy()
        self.fallenshapes.append(tempshape)
        self.currentShape = Shape(self.screen)


    def main(self):

        while(self.playing):
            self.screen.erase()#clear screen
            self.draw()
            if(self.collide()==False):
                self.currentShape.y+=1
            else:
                self.land()
            time.sleep(0.5)

def inputs(main):
    while(True):
        c = main.screen.getch()
        if (str(c) == "119"):
            main.currentShape.rotate(1)
        if (str(c) == "100"):
            main.currentShape.x +=1
        if (str(c) == "97"):
            main.currentShape.x -=1
        if (str(c) == "115"):
            main.currentShape.rotate(2)
        if(str(c) == "113"):
            main.playing = False
            break

main = Main()
x = threading.Thread(target=inputs,args=(main,))
x.start()
main.main()
curses.endwin()

