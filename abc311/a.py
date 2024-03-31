# n,k = map(int,input().split())
n = int(input())
s = input()
visit = set()
for i,v in enumerate(s):
    visit.add(v)
    if len(visit) == 3:
        print(i+1)
        exit()

# A = list(map(int,input().split()))