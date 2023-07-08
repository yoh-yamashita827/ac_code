a,b = map(int, input().split())
A = str(a)
B = str(b)
a_lis = list(map(int, A))
b_lis = list(map(int, B))
l_a = len(a_lis)
l_b = len(b_lis)

if l_a < l_b:
    a_lis,b_lis = b_lis,a_lis

a_pre = list(reversed(a_lis))
b_pre = list(reversed(b_lis))

flg = False

for i in range(len(b_pre)):
    if a_pre[i] + b_pre[i] >= 10:
        flg = True    
        break

if flg:
    print('Hard')
else:
    print('Easy')