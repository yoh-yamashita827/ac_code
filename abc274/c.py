# n = int(input())
# n,m = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
# s = []
# for _ in range(n):
#     s.append(input())

N=int(input())
A=list(map(int,input().split()))
ans=[0]*(2*N+1)
for i,a in enumerate(A):
  ans[2*i+1]=ans[a-1]+1
  ans[2*i+2]=ans[a-1]+1

print(*ans,sep="\n")
