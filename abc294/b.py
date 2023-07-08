h,w = map(int,input().split())

a = []
for i in range(h):
    a.append(list(map(int,input().split())))

al = [chr(i) for i in range(65, 65+26)]
# [chr(i) for i in range(ord('A'), ord('Z')+1)]

for i in range(h):
    ans = []
    for j in range(w):
        num = a[i][j]
        if num == 0:
            ans.append('.')
        else:
            ans.append(al[num-1])

    print(''.join(ans))