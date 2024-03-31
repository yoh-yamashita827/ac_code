n = int(input())
# n,m = map(int,input().split())
# s = input()
d = list(map(int,input().split()))
# s = []
# for _ in range(n):
#     s.append(input())
cnt = set()

for m,day in enumerate(d):
    m = m+1
    for dd in range(1,day+1):
        tmp = list(str(m)+str(dd))
        if len(set(tmp)) == 1:
            cnt.add((m,dd))

print(len(cnt))
# print(cnt)