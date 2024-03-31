n = int(input())
A = []
for i in range(n):
   c = int(input())
   A.append(list(map(int,input().split())))

x = int(input())
cdd = []
for i,v in enumerate(A):
   if x in v:
      cdd.append((i+1,len(v)))

if cdd == []:
   print(0)
   exit()

min_c = min(cdd,key=lambda x:x[1])

ans = []
for i in cdd:
   if i[1] == min_c[1]:
      ans.append(i[0])

ans.sort()
print(len(ans))
print(*ans)
