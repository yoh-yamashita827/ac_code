n = int(input())
# n,m = map(int,input().split())
s = input()
# c = list(map(int,input().split()))
# s = []
# for _ in range(n):
#     s.append(input())


def a_to_num(str):
    if str == 'R':
        return 0
    elif str == 'L':
        return 1
    elif str == 'U':
        return 2
    else:
        return 3
    
dx = [1,-1,0,0]
dy = [0,0,1,-1]

rireki = set()
now = (0,0)
rireki.add(now)
for i in s:
    now = (now[0]+dx[a_to_num(i)],now[1]+dy[a_to_num(i)])

    if now in rireki:
        print('Yes')
        exit()
    rireki.add(now)
print('No')