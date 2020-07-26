import maze
c = maze.Connect("oof2win2", "tojedalka")
while True:
    if not c.move('s'):
        print('error moving, error code', error)
    if not c.move('d'):
        print('error moving, error code', error)
    if not c.move('w'):
        print('error moving, error code', error)
    if not c.move('a'):
        print('error moving, error code', error)