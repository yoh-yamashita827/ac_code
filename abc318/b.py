n = int(input())
# n,m = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
N = 101
grid = [[0]*(N) for _ in range(N)]

for _ in range(n):
   a,b,c,d = map(int,input().split())
   grid[c][a] += 1
   grid[c][b] -= 1
   grid[d][a] -= 1
   grid[d][b] += 1

n = N
for y in range(n):
   for x in range(1,n):
        grid[y][x] += grid[y][x-1]


for y in range(1,n):
    for x in range(n):
        grid[y][x] += grid[y-1][x]

ans = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] >= 1:
            ans +=1

print(ans)