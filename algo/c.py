n = int(input())

num = set(range(2,2*n+2))
print(1)
exist = set()
exist.add(1)
a = 1
while(a != 0):
   a = int(input())
   exist.add(a)

   mod = num-exist
   tmp = next(iter(mod))
   print(tmp)
   exist.add(tmp)
