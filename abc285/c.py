# N,M = map(int,input().split())
# A = list(map(int,input().split()))
S = []
# for _ in range(N):
#    S.append(input())
# 
mod = 65
def make_number(s):
   ans = 0
   for i,v in enumerate(reversed(s)):
      ans += ((ord(v)%mod)+1)*(26**i)

   return ans
print(make_number(input()))