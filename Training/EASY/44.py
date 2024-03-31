s = list(input())
s = [int(i) for i in s]
import copy 

S = copy.deepcopy(s)

def cnt_osero(start):
    cnt = 0
    for i in S:
        if i!=start:
            cnt += 1
        start = abs(1-start)

    return cnt

print(min(cnt_osero(0),cnt_osero(1)))


