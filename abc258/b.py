# n = int(input())
# # n,m = map(int,input().split())
# # s = input()
# # c = list(map(int,input().split()))
# a = []
# for _ in range(n):
#    tmp = list(input())
#    tmp = [int(i) for i in tmp]
#    a.append(tmp)

# grid = []
# for i in range(3):
#     for j in a:
#         grid.append(j*4)

# id = (0,0)
# max_a = 0
# for i in range(n):
#     for j in range(n):
#         if a[i][j] > max_a:
#             max_a = a[i][j]
#             id = (i,j)


# ans = [grid[id[0]][id[1]]]
# y = id[0]+n
# x = id[1]+n
# for i in range(n):
#     ans.append(max(grid[y-1][x],grid[y+1][x],grid[y][x-1],grid[y][x+1],grid[y+1][x+1],grid[y+1][x-1],grid[y-1][x+1],grid[y-1][x-1]))

# print(*ans)


N=int(input())
A=[list(input()) for _ in range(N)]

d=((1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1))
ans=0
for i in range(N):
    for j in range(N):
        for dy,dx in d:
            num=""
            for k in range(N):
                num+=A[(i+dy*k)%N][(j+dx*k)%N]
            ans=max(ans,int(num))

print(ans)
