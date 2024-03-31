# n = int(input())
h,w = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
s = [list(input()) for _ in range(h)]
# for _ in range(n):
#     s.append(input())
zahyo = set()
cnt = 0
dx = [0,-1,1,0,0,-1,1,1,-1]
dy = [0,0,0,-1,1,-1,1,-1,1]

for i in range(h):
    for j in range(w):
        flg = False
        if s[i][j] == '#':
            for xy in range(9):
                tmp_x = i+dx[xy]
                tmp_y = j+dy[xy]

                if (tmp_x > h-1) or (tmp_y > w-1):
                    continue
                if s[tmp_x][tmp_y] == '#':
                    flg = True

                if not flg:
                    cnt += 1
                

print(cnt)






