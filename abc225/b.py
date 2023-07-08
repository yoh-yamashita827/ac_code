
N = int(input())
l = []
edge = []
c = []

for i in range(N-1):
    a,b = input().split()
    l.append([int(a),int(b)])


for i in range(N-2):
    c = list(set(l[i]) & set(l[i+1]))
    if len(set(c)) == 0:
        print ('No')
        exit(0)
    edge.append(c[0])



if len(set(edge)) == 1:
    print('Yes')
else:
    print('No')

