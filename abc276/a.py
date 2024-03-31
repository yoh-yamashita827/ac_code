#N = int(input())
#N,M = map(int,input().split())
S = input()
#A = list(map(int,input().split()))
#S = []
#for _ in range(N):
   #S.append(input())
a = S.rfind('a')
if a == -1:
   print(-1)
else:
   print(a+1)
