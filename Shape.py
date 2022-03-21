import numpy as np
import curses
from shapes import getRandomShape

class Shape:

    # shape=[[0,1,0,0],
    #        [0,1,0,0],
    #        [0,1,0,0],
    #        [0,1,0,0]]
    shape=[[0,0,0,0],
           [0,0,0,0],
           [0,0,1,0],
           [0,1,1,1]]
    points = []

    x = 5
    y = 2
    def __init__(self,screen):
        self.screen = screen
        self.shape = getRandomShape()[0]


    def rotate(self,dire):
        m = np.array(self.shape,int)
        if(dire==1):
            self.shape = np.rot90(m)
        else:
            self.shape = np.rot90(m)
            self.shape = np.rot90(m)
            self.shape = np.rot90(m)

    def copy(self):
        temps = Shape(self.screen)
        temps.x = self.x
        temps.y = self.y
        temps.shape = self.shape
        return temps

    def drawShape(self):
        y = 0
        i = 0
        self.points = []
        for row in self.shape:
            for b in row:
                if(b==1):
                    self.points.append([i+self.x,y+self.y])
                    self.screen.addstr(y+self.y,i+self.x,"*")
                i+=1
            i=0
            y+=1
        self.screen.refresh()
