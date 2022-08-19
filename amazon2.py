 #initial inputs for creating the environment: number of rows h, number of columns l, 
 #starting point, end point, obstacles.
 #h, l are integers; start, end are lists of len = 2; obs is a list of lists, 
 #each component of the list obs indicates the position (y, x) of one obstacle.
import math
 
def shpath(h, l, start, end, obs):
    n = [[0 for j in range(l)] for i in range(h)]
    dist = [[math.inf for j in range(l)] for i in range(h)]
    q = []
    path = []
    
    for k in range(len(obs)):
        n[obs[k][0]][obs[k][1]] = 1
    
    #n[start[0]][start[1]] = 2
    #n[end[0]][end[1]] = 3
    
    dist[start[0]][start[1]] = 0
    q.append(start)
    
    while len(q) > 0:
        v = q.pop(0) # v = q.pop(-1)
        path.append(v)
        # for each neighbor w of v...
        for i in range(-2, 2):
            for j in range(-2, 2):
                w = [v[0] + i, v[1] + j]
                if -1 < w[0] < h and -1 < w[1] < l:
                    if n[w[0]][w[1]] != 1:
                        if dist[w[0]][w[1]] > dist[v[0]][v[1]]+1: # > math.inf
                            q.append(w)
                            dist[w[0]][w[1]] = dist[v[0]][v[1]] + 1
                        if w == end:
                            if dist[w[0]][w[1]] != math.inf:
                                path.append(end)
                                return path, dist[end[0]][end[1]]
    s = 'impossible to reach'
    return s
    
        
        
    
    
    
