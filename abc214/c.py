N = int(input())
S = list(map(int,input().split()))
T = list(map(int,input().split()))
ans = []
ans2 = []

ans.append(T[0]) # first man 
time = S[0]+T[0]

for i in range(1,N): # from sunuke or takashi
    c = min(time,T[i])
    time = c
    ans.append(time)
    time += S[i]
   
if T[0] > time: # from last or takashi
    ans[0] = time
else:
    for i in ans:
        print(i)
    exit(0)


ans2.append(time)

time += S[0]

for i in range(1,N):
    c = min(time,ans[i])
    time = c
    ans2.append(time)
    time += S[i]


for i in ans2:
    print(i)

