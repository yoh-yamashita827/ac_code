N = int(input())
ans = []
for i in reversed(range(int(N**(1/2)+1))):
    if i == 0:
        continue
    elif N % i == 0:
        if i**2 == N:
            ans.append(i)
            continue
        ans.append(N//i)
        ans = [i]+ans

for j in (ans):
    print(j)


