n,k = map(int,input().split())

md = []
total = 0
for _ in range(n):
    a,b = map(int,input().split())
    total += b
    md.append((a,b))

med = sorted(md,key=lambda x:x[0])

if total <= k:
    print(1)
    exit()

for i,v in enumerate(med):
    total -= v[1]
    if total <= k:
        print(v[0]+1)
        exit()
