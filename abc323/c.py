# n = int(input())
n,m = map(int,input().split())
# s = input()
A = list(map(int,input().split()))
s = [input() for _ in range(n)]
# for _ in range(n):
#     s.append(input())

from collections import defaultdict
now_point = defaultdict(int)
nokori_point = defaultdict()

for v,i in enumerate(s):
    tmp = []
    for j in range(len(i)):
        if i[j] == 'o':
            now_point[v] += A[j]
        else:
            tmp.append(A[j])

    now_point[v] += (v+1)
    
    if tmp != []:
        tmp.sort(reverse=True)
        # mt = [0]
        # for ii, aa in enumerate(tmp):
        #     mt.append(mt[ii] + aa)

    nokori_point[v] = tmp

            
point_max = max(now_point.values())

for k,v in now_point.items():
    if v == point_max:
        print(0)
        continue

    point = v
    for ii,mm in enumerate(nokori_point[k]):
        point += mm
        if (point) > point_max:
            print(ii+1)
            break

    
