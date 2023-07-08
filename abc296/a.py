n = int(input())
s = list(input())

for i in range(len(s)-1):
  now = s[i]
  next = s[i+1]
  if now != next:
    continue
  else:
    print('No')
    exit()
  
print('Yes')