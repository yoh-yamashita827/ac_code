N,A,B = map(int,input().split())
S = (input())
# A = list(map(int,input().split()))
# S = []
# for _ in range(N):
#    S.append(input())
S += S
def funcA(List):
   tmp = List.pop(0)
   List.append(tmp)

ans = 1 << 60


tmp = 0
for j in range((N//2)):
   if S[j] != S[N-j-1]:
      tmp += B
ans = min(ans,tmp)

for i in range(1,N):
   # funcA(S)
   tmp = i*A
   for j in range((N//2)):
      if S[i+j] != S[i+N-j-1]:
         tmp += B
   ans = min(ans,tmp)

print(ans)


