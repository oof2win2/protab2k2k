import maze
import time

#dfs for A2
#TODO:
#   - get the vertexes from the function c.get_all()
#   - make the whole program work with a 2-dimensional array


c = maze.Connect("oof2win2", "vylet")
c.wait()

def neighbors(vertex):
    #finds the neighbors of the vertex
    graph = c.get_all()
    return graph[vertex]


#should work for everything on Protab2k2k
def dfs(startx, starty, endx, endy):
    #finds the path from start to end in a graph using the function neighbors(). will run forever if a path doesnt exist
    visited = set()
    path = [[startx, starty]]
    while True:
        done = False
        if path[-1] == [endx, endy]:
            return path
        #move to a different vertex
        for n in neighbors(path[-1]):
            if n not in visited:
                visited.add(n)
                path.append(n)
                done = True
                break
                
        #go back
        if not done:
            path.pop(-1)
path = dfs(c.x(), c.y())
print(path)