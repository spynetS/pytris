import time
import os
import curses
import threading


from Shape import Shape

#q 113
#d 100
#a 97
#s 115
#w 119
playing = True
shape1 = Shape("")
fallenshapes = []
width = 15
height = 15
screen = curses.initscr()

def inputs(screen):
    global playing
    global shape1
    while(True):
        c = screen.getch()
        if (str(c) == "119"):
            shape1.rotate(1)
        if (str(c) == "100"):
            shape1.x +=1
        if (str(c) == "97"):
            shape1.x -=1
        if (str(c) == "115"):
            shape1.rotate(2)

        if(str(c) == "113"):
            playing = False
            break

def collide():
    global height
    for p in shape1.points:
        if(p[1]+1 >= height):
            return True
        for shape in fallenshapes:
            for p1 in shape.points:
                if(p[0]==p1[0] and p1[1]==p[1]+1):
                    return True

    return False

def drawGround():
    global screen
    global height
    global width
    for x in range(width):
        screen.addstr(height,x,"#")

screen = curses.initscr()


x = threading.Thread(target=inputs,args=(screen,))
x.start()

shape1 = Shape(screen)

while(playing):
    screen.erase()
    drawGround()
    shape1.drawShape()
    for shape in fallenshapes:
        shape.drawShape()

    if(collide()==False):
        shape1.y+=1
    else:
        tempshape = shape1.copy()
        fallenshapes.append(tempshape)
        shape1 = Shape(screen)
    time.sleep(0.5)

curses.endwin()

