n = int(input())
# n,m = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))

n2 = bin(n)[2:]
mask = []

for id,i in enumerate(n2):
    if i == '1':
        mask.append(id)

## bit search
N = len(mask)
ans = []
for i in range(2**N):
    num = list(n2)
    for j in range(N):
        if i >> j & 1: # select J?
            num[mask[j]] = '0'

    ans.append(int(''.join(num),2))

ans.sort()

for i in ans:
    print(i)