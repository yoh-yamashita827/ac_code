# n = int(input())
h,w = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
map = [list(input()) for _ in range(h)]
# for _ in range(n):
#     s.append(input())

# t_map = zip(*map)
cnt = 0
ans = []
for i in range(w):
    for j in range(h):
        if map[j][i] == '#':
            cnt += 1

    ans.append(cnt)
    cnt = 0

print(*ans)