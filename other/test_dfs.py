def sousedi(vrchole):
    #najde sousedy vrcholu vrchol v grafu 
    pass

def dfs(start, cil):
    #najde path v grafu podle startu a cile, pouziva funkci sousedi
    navstiveno = set(start)
    cesta = [start]
    while True:
        vrchol = cesta[-1]
        