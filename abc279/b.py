#N = int(input())
#N,M = map(int,input().split())
S = input()
T = input()

s = len(S)
t = len(T)

if t > s:
    print('No')
    exit()
#A = list(map(int,input().split()))
#S = []
#for _ in range(N):
   #S.append(input())

for i in range(s-t+1):
    if S[i:i+t] == T:
        print('Yes')
        exit()

print('No')

        