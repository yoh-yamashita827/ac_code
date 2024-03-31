# n = int(input())
a,b,c,d,e,f = map(int,input().split())
nums = [a,b,c,d,e,f]
mod = 998244353
nums_mod = [i%mod for i in nums]
# s = input()
# c = list(map(int,input().split()))
# s = []
# for _ in range(n):
#    s.append(input())



print(((a*b*c)%mod-(d*e*f)%mod)%mod)