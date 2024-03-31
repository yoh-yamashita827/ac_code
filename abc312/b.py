#N = int(input())
N,M = map(int,input().split())
#S = input()
#A = list(map(int,input().split()))
S = []
for _ in range(N):
   S.append(list(input()))

import numpy as np

S = np.array(S)

tak = ['###.ooooo','###.ooooo','###.ooooo','....ooooo','ooooooooo','ooooo....','ooooo.###','ooooo.###','ooooo.###']

tak = np.array([list(i) for i in tak])

for i in range(N-9+1):
   for j in range(M-9+1):
      window = S[i:i+9,j:j+9]
      if sum(sum(window==tak)) == 32:
         print(i+1,j+1)

