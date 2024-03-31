#N = int(input())
N,M = map(int,input().split())
#S = input()
A = list(map(int,input().split()))
B = list(map(int,input().split()))
#S = []

def binary_search(keys,x):
   l = 0
   r = len(keys)

   while(r!=l):
      m = (l+r)//2
      if keys[m] > x:
         r = m
      else:
         l = m+1

   return l

# A.sort()
# B.sort()

if min(A) > max(B):
   print(max(B)+1)
   exit()


A.sort()
B.sort()

for i in A:
   a = binary_search(A,i)
   b = binary_search(B,i)

   if a >= (N-b):
      print(i)
      exit()