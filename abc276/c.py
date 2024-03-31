N = int(input())
#N,M = map(int,input().split())
#S = input()
P = list(map(int,input().split()))


id_1 = P.index(1)

ans = []
all_nums = list(range(1,N+1))

for i in range(id_1):
   ans.append(P[i])
   all_nums.remove(P[i])

all_nums.sort(reverse=True)

print(*(ans+all_nums))

