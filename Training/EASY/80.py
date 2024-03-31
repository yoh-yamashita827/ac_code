def devide_list(N):
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

    return ans

n = int(input())

div = devide_list(n)
div2 = div[::-1]
ans = INF=float('inf')
for i,j in zip(div,div2):
    ans = min(ans,i+j)

print(ans-2)