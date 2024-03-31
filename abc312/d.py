#N = int(input())
#N,M = map(int,input().split())
S = input()
#A = list(map(int,input().split()))
#S = []
#for _ in range(N):
   #S.append(input())

mod = 998244353

question = S.count('?')

if question == 0:
   print(0)
   exit()

que = ''
ans = 1
for i in S[::-1]:
   if (i != '(') and (i != ')'):
      que += i

   else:
      if que.count('?') %2 != 0:
         ans *= 2**((que.count('?')-1)//2)%mod
         que = ''

      else:
         ans *= 2**((que.count('?'))//2)%mod
         que = ''

print(ans%mod)