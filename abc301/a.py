N = int(input())
S = list(input())

T = S.count('T')
A = S.count('A')

if len(S) == 1:
  print(S[0])
  exit()

if T > A :
  print('T')
  
elif A > T :
  print('A')
  
else:
  if S[-1] == 'T':
    print('A')
  else:
    print('T')