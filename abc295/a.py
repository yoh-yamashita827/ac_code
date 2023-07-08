n = int(input())
w = list(map(str,input().split()))
cdd = ['and','not','that','the','you']

for i in w:
  if i in cdd:
    print('Yes')
    exit()
    
print('No')