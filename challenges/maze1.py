import maze
c = maze.Connect("oof2win2", "vyhlidka")

if not c.move('s'):
    print('error moving, error code', error)
width = c.width()
height = c.height()
