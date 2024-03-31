#N = int(input())
#N,M = map(int,input().split())
S = input()
#A = list(map(int,input().split()))
#S = []
#for _ in range(N):
   # S.append(input())

ans = ''
for i in S:
   if i == '0':  
      ans += '1'
   elif i == '1':
      ans += '0'

print(ans)
