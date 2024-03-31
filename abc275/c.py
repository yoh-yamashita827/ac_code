# n = int(input())
# n,m = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
import numpy as np

s = []
for _ in range(9):
   s.append(list(input()))

ans = 0
for y in range(9):
   for x in range(9):
        if s[y][x] == '#':

            l = min(9-x,9-y)
            for i in range(1,l):
                a = s[y][x+i]
                b = s[y+i][x]
                c = s[y+i][x+i]
                if (a==b==c=='#'):
                    ans += 1

print(ans)