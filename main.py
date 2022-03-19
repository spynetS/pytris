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
height = 10

def inputs(screen):
    global playing
    global shape1
    while(True):
        c = screen.getch()
        #screen.addstr(0,0,str(c))
        if (str(c) == "119"):
            shape1.rotate(1)
        if (str(c) == "100"):
            shape1.x +=1
        if (str(c) == "97"):
            shape1.x -=1
        if (str(c) == "115"):
            shape1.rotate(2)

        if(str(c) == "113"):
            screen.addstr(0,0,str(c))
            playing = False
            break

def collide():
    global height
    for p in shape1.points:
        if(p[0]+1 >= height):
            pass
    return False


screen = curses.initscr()

x = threading.Thread(target=inputs,args=(screen,))
x.start()

shape1 = Shape(screen)

while(playing):
    screen.erase()
    shape1.drawShape()
    for shape in fallenshapes:
        shape.drawShape()

    if(collide()==False):
        shape1.y+1
    else:
        tempshape = shape1.copy()
        fallenshapes.append(tempshape)
        shape1 = Shape(screen)
    time.sleep(0.5)

curses.endwin()

