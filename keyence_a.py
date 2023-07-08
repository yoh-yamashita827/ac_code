n,k,a = map(int,input().split())
if (k+a-1)%n == 0:
  print(n)
  exit()
print((k+a-1)%n)

