N = int(input())
#N,M = map(int,input().split())
#S = input()
#A = list(map(int,input().split()))
S = []
visit  = set()
for _ in range(N):
   tmp = input()
   S.append(tmp)
   visit.add(tmp)

if len(visit) != N:
   print('No')
   exit()

q1 = ['H','D','C','S']
q2 = ['A','2','3','4','5','6','7','8','9','T','J','K','Q']
for i in S:
   if (i[0] not in q1) or (i[1] not in q2):
      print('No')
      exit()

print('Yes')
