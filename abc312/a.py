#N = int(input())
#N,M = map(int,input().split())
#S = input()
#A = list(map(int,input().split()))
#S = []
#for _ in range(N):
   #S.append(input())

S = input()
tmp = ['ACE','BDF','CEG','DFA','EGB','FAC','GBD']
if S in tmp:
   print('Yes')
else:
   print('No')