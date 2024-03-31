#N = int(input())
N,M = map(int,input().split())
if N < M:
   print(*([0]*N))
   exit()
#S = input()
A = list(map(int,input().split()))
#S = []
#for _ in range(N):
   #S.append(input())

for i in range(M):
   A.pop(0)

for i in range(M):
   A.append(0)

print(*A)