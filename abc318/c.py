# n = int(input())
n,d,p = map(int,input().split())
# s = input()
f = list(map(int,input().split()))
# s = []
# for _ in range(n):
#    s.append(input())

f.sort(reverse=True)
ans = sum(f)
box = []
i = 0
while(i < n):
    if len(box) == d:
        if sum(box) > p:
            ans -= sum(box)
            ans += p
        box = []

    box.append(f[i])
    i += 1

if sum(box) > p:
    ans -= sum(box)
    ans += p
print(ans)


    

