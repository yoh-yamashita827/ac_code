r,c = map(int,input().split())
b = []

for i in range(r):
    b.append(list(input()))
import copy
map = copy.deepcopy(b)
import numpy as np    

for x in range(r):
    for y in range(c):
        if b[x][y].isdigit():    
            d = int(b[x][y])        
            base = np.array([x,y])
            for i in range(r):
                for j in range(c):
                    ags = np.array([i,j])
                    if int(np.linalg.norm(base-ags,ord=1)) <= d:
                        map[i][j] = '.'
    
for i in map:
    print("".join(i))
            