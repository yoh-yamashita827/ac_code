n,m = map(int,input().split())
if m != n-1:
    print('No')
    exit()

from collections import defaultdict


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())
uf = UnionFind(n)
deg = [0]*n
for _ in range(m):
    a,b = map(int,input().split())
    deg[a-1] += 1
    deg[b-1] += 1
    uf.union(a-1,b-1)

if len(list(uf.all_group_members())) != 1:
    print('No')
    exit()

c1 = 0
c2 = 0
for i in deg:
    if i == 1:
        c1 += 1
    elif i == 2:
        c2 += 1

if (c1 == 2) and (c2 == (n-2)):
    print('Yes')
else:
    print('No')