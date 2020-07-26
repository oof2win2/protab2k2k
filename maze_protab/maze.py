maze = \
"""
#######
#..F#.#
#.###.#
#.....#
#####.#
#S....#
#######
"""
maze2 = []
maze = maze.strip().splitlines()
for i in range(len(maze)):
    for j in range(len(maze[0])):
        maze2.append(maze[i][j])
maze = maze2
#from now on, the maze is a list of chars

#S = start
#F = finish
## = wall
#. = blank

#to iterate in maze use global variables WIDTH and HEIGHT like this:
#       maze[HEIGHT*row+column]
WIDTH  = 7
HEIGHT = 7
#prints the maze
def printMaze():
    line = []
    for i in range(WIDTH):
        for j in range(HEIGHT):
            line.append(maze[i*HEIGHT+j])
        print("".join(line))
        line = []
    print("\n")

#gets the X and Y coords of the "S" character
def getXY():
    for i in range(WIDTH):
        for j in range(HEIGHT):
            if (maze[i*WIDTH+j] == "S"):
                return [i, j]

#moves left once
def moveLeft(): 
    x, y                    =  getXY()
    if (maze[x*WIDTH+(y-1)] == "."): 
        maze[x*WIDTH+y]     =  "."
        maze[x*WIDTH+y-1]   =  "S"
    else                    :  
        print("CANNOT GO LEFT.")
    return

#moves right once
def moveRight(): 
    x, y                    =  getXY()
    if (maze[x*WIDTH+(y+1)] == "."): 
        maze[x*WIDTH+y]     =  "."
        maze[x*WIDTH+y+1]   =  "S"
    else                    :  
        print("CANNOT GO RIGHT.")
    return

#moves down once
def moveDown():
    x, y                    =  getXY()
    if (maze[(x+1)*WIDTH+y] == "."): 
        maze[(x)*WIDTH+y] =  "."
        maze[(x+1)*WIDTH+y] =  "S"
    else                    :  
        print("CANNOT GO DOWN.")
    return

#moves up once
def moveUp():
    x, y                    =  getXY()
    if (maze[(x-1)*WIDTH+y] == "."): 
        maze[(x)*WIDTH+y] =  "."
        maze[(x-1)*WIDTH+y] =  "S"
    else                    :  
        print("CANNOT GO UP.")
    return

printMaze()