# n = int(input())
n,q = map(int,input().split())
s = input()
# c = list(map(int,input().split()))
# s = []
# for _ in range(n):
#     s.append(input())

ss = [0]*(n+1)

pre = '0'
for i,v in enumerate(s):
    if v==pre:
        ss[i] = 1
    pre = v

mt = [0]
for i, aa in enumerate(ss):
  mt.append(mt[i] + aa)


for _ in range(q):
    l,r = map(int,input().split())
    print(mt[r]-mt[l])
