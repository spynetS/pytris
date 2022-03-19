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
    for shape in fallenshapes:
        for p1 in shape1.points:
            for p2 in shape.points:
                for x in p1:
                    for y in p2:
                        if(x[0]==y[0] and (x[1]+1) == y[1]):
                            return True
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
    if (collide()):
        shape1.y+1
    if(shape1.y<6):
        shape1.y+=1
    else:
        tempshape = shape1.copy()
        fallenshapes.append(tempshape)
        shape1 = Shape(screen)
    time.sleep(0.5)

curses.endwin()

