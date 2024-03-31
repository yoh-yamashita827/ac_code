## bit search
def bit_search():
   for i in range(2**N):
      total = 0
      for j in range(N):
         if i >> j & 1: # select J?
            total += list[j]
      if total == x:
         print(x)
         break