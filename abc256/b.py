n = int(input())
# n,m = map(int,input().split())
# s = input()
A = list(map(int,input().split()))
# s = []
# for _ in range(n):
#     s.append(input())
ans = []
for i in A:
    
    for j in range(len(ans)):
        ans[j] += i

    ans.append(i)

cnt = 0
for i in ans:
    if i >= 4:
        cnt += 1

print(cnt)