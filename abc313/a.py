N = int(input())
#N,M = map(int,input().split())
#S = input()
A = list(map(int,input().split()))
#S = []
#for _ in range(N):
   #S.append(input())
if N == 1:
   print(0)
   exit()
s = max(A[1:])

if A[0] > s:
   print(0)
else:
   print(s-A[0]+1)