#N = int(input())
N,M = map(int,input().split())
#S = input()
A = list(map(int,input().split()))
#S = []
#for _ in range(N):
   #S.append(input())
from collections import defaultdict
m_dict = defaultdict(int)
for v,i in enumerate(range(N-M+1)):
   window = A[i:i+M]
   m_dict[v] = (sum(window))

# sort(key=lambda x:x[1],reversed=True)
sorted(m_dict.items(),key=lambda x:x[1],reverse=True)
ans = 0

max_window = list(m_dict.keys())[0]

for ii,vv in A[max_window:max_window+M]:
   ans += (ii+1)*vv

print(ans)