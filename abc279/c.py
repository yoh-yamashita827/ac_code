#N = int(input())


H,W = map(int,input().split())
#S = input()
#A = list(map(int,input().split()))
from collections import defaultdict

S = []
for _ in range(H):
   S.append(list(input()))
   # S[tmp]

T = []
for _ in range(H):
   T.append(list(input()))



Snp = list(zip(*S))
Tnp = list(zip(*T))

S_dic = defaultdict(int)
T_dic = defaultdict(int)
S_edge = set()
for i in Snp:
   S_edge.add(tuple(i))
   S_dic[tuple(i)] += 1

T_edge = set()
for j in Tnp:
   T_edge.add(tuple(j))
   T_dic[tuple(j)] += 1

if S_edge == T_edge:
   for key in S_dic.keys():
      if S_dic[key] != T_dic[key]:
         print('No')
         exit()
   print('Yes')
else:
   print('No')