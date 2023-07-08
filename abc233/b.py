l,r = map(int,input().split())
s = input()
S = list(s)
a = []

for i in range(l-1,r):
    a.append(S[i])


for i in range(l-1,r):
    S[i] = a.pop()

strS = ''.join(S)

print(strS)