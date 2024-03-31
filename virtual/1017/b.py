# n = int(input())
n,m = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
# s = []
# for _ in range(n):
#     s.append(input())
import itertools
graph = [[-1]*n for _ in range(n)]

for i in range(m):
    inp = (list(map(int,input().split())))
    k,x = inp[0],inp[1:]
    for j in itertools.combinations(x,2):
        graph[j[0]-1][j[1]-1] = 1
        graph[j[1]-1][j[0]-1] = 1

for i in range(n):
    for j in range(n):
        if (i == j) and graph[i][j] != -1:
            print('No')
            exit()
        elif (i!= j) and graph[i][j] != 1:
            print('No')
            exit()
print('Yes')