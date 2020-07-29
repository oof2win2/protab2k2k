from tqdm import tqdm
from collections import Counter
import maze
import keyboard
import time
import sys
import random

#CAUTION: DOESNT WORK AS OF NOW

c = maze.Connect("oof2win2", "vylet")
area = []

#chest = 3
#wall  = 2
#blank = 0

height = c.height
width = c.width
x = c.x()
y = c.y()
print(x, y)

area = c.get_all()
orig_area = area

print('done collecting')
area[x][y] = -5 #set the starting thing to already walked
#prints the area out as a list
def printArea():
    for i in range(height):
        arr = []
        for j in range(width):
            arr.append(area[i][j])
        print(*arr, sep = '')


#returns list with x, y coordinates of thing from number
def getPos(thing):
    for i in range(height):
        for j in range(width):
            if (area[i][j] == thing):
                return [i, j]


    for j in range(width):
        char = str(area[i][j])
        if char == '0':
            original.write('.')
        elif char == '2':
            original.write('#')
        elif char == '3':
            original.write('K')
        else:
            original.write('?')
    original.write('\n')

#moves using deltax, deltay
def move(dx, dy):
    global x
    global y
    if (area[x+dx][y+dy] == 0):
        area[x+dx][y+dy] = -5
        #-5 = places went to
        x += dx
        y += dy
        return 1
    elif area[x+dx][y+dy] == 3:
        return 3
    else:
        return 0


#attempts to move, first right, then in other directions
#returns 1 when succesfull, 0 when wall hit, 3 when chest hit (game won)
def tryMove():
    print('trying move from coords')
    dir = [[0, 1], [1, 0], [-1, 0]]
    sucess = 0
    choose = 0
    while sucess != 1:
        choose = random.randint(0, 1000) % 3
        a = move(dir[choose][0], dir[choose][1])
        if a == 3:
            sucess = 3
            return 3
        elif a == 0:
            sucess = 0
        elif a == 1:
            sucess = 1
        c.x()

def searchAround(x, y, obj):
    print('searching around point', x, y)
    if (area[x+1][y] == obj):
        return [x+1, y]
    elif (area[x-1][y] == obj):
        return [x-1, y]
    elif (area[x][y+1] == obj):
        return [x, y+1]
    elif (area[x][y-1] == obj):
        return [x, y-1]
    else:
        print('couldnt find.')
        sys.exit()

def doMove(orig_area, modified_area):
    x = c.x()
    y = c.y()
    cx, cy = getPos(3)                   #gets xy of chest
    modified_area[x][y] = 2     #walls in the start position
    while (x != cx and y != cy):
        x = c.x()
        y = c.y()
        dx, dy = searchAround(x, y, -5)
        x -= dx
        y -= dy

        if x != 0:
            if x > 0:
                c.move('d')
            elif x < 0:
                c.move('a')
        elif y != 0:
            if y > 0:
                c.move('w')
            if y < 0:
                c.move('s')
        modified_area[x, y] = 2 #walls the player from behind

def run():
    i = 0
    while True:
        i += 1
        print('running the', i, 'time')
        a = tryMove()
        if a == 3:
            print('game won')
            doMove(orig_area, area)

run()