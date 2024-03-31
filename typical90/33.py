h,w = map(int,input().split())

import math
if (h==1) or (w==1):
    print(h*w)
else:   
    print(int(math.ceil(h/2)*math.ceil(w/2)))