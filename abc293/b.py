n = int(input())
A = list(map(int,input().split()))

member = set([i for i in range(1,n+1)])
called = set()

for i,v in enumerate(A):
    if (i+1) not in called:
        if v not in called:
            member.remove(v)
        called.add(v)

print(len(member))
print(*member)