n,k,q = map(int,input().split())
score = [k-q]*n

for _ in range(q):
    a = int(input())
    score[a-1]+=1

for i in score:
    if i > 0:
        print('Yes')
    else:
        print('No')