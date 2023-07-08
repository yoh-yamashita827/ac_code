n,x,y,z = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = []
for a,b in zip(A,B):
    C.append(a+b)
math = {}
eng = {}
total = {}

for i,v in enumerate(A):
    math[i] = v
for i,v in enumerate(B):
    eng[i] = v
for i,v in enumerate(C):
    total[i] = v

math = sorted(math.items(), key=lambda x:x[1],reverse=True)
eng = sorted(eng.items(), key=lambda x:x[1],reverse=True)
total = sorted(total.items(), key=lambda x:x[1],reverse=True)

ans = set()


for i in math:
    if len(ans) == x:
        break
    ans.add(i[0])

for i in eng:
    if len(ans) == x+y:
        break
    ans.add(i[0])

for i in total:
    if len(ans) == x+y+z:
        break
    ans.add(i[0])

ans = sorted(list(ans))
for i in ans:
    print(i+1)