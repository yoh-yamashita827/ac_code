n = int(input())

table = []

for i in range(n):
    a,b=input().split()
    table.append([a, int(b)])
mini = 10000000000
for ii,i in enumerate(table):
    if (i[1]) < mini:
        mini = (i[1])
        min_id = ii

for j in range(n):
    if min_id == n:
        min_id = 0
    print(table[min_id][0])
    min_id += 1


