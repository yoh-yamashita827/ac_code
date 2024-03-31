import sys
sys.setrecursionlimit(10**6)
N = int(input())
#N,M = map(int,input().split())
#S = input()
A = list(map(int,input().split()))





def average(A:list):   
   new_list = []

   A.sort()

   i = 0
   ans = 0
   while(i != N//2):
      min_v,max_v = A[i],A[-i-1]
      if (min_v+max_v)%2 == 0:
         new_list.append((min_v+max_v)//2)
         new_list.append((min_v+max_v)//2)
      else:
         new_list.append((min_v+max_v)//2)
         new_list.append(((min_v+max_v)//2)+1)
         
      ave_v = (min_v+max_v)//2
      ans += (ave_v-min_v)
      i += 1
   return ans,new_list

ans = 0
cnt,A = average(A)


print(cnt+1)