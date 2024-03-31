#N = int(input())
N,M = map(int,input().split())
#S = input()
#A = list(map(int,input().split()))
#S = []
#for _ in range(N):
   #S.append(input())
all_set = []
for i in range(M):
   c = int(input())
   A = set(map(int,input().split()))

   all_set.append(A)

## bit search
cnt = 0
all_num = set(range(1,N+1))

for i in range(2**M):
   total = set()
   for j in range(M):
      if i >> j & 1: # select J?
         total |= all_set[j]
   if total == all_num:
      cnt += 1
      

print(cnt)

