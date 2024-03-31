import math
import numpy as np
t = int(input())
l,x,y = map(int,input().split())
q = int(input())

for _ in range(q):
    e = int(input())

    e_x = (l/2)*(1-math.cos(e))
    e_y = (l/2)*(1+math.sin(e))

    e_vec = np.array([0,e_x,e_y])
    against = np.array([x,y,0])
    vec = against-e_vec
    
    
    theta = math.acos(np.dot(vec,against)/(np.linalg.norm(vec,ord=2)*np.linalg.norm(against,ord=2)))

    print(math.degrees(theta))