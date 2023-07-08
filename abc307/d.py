n = int(input())
S = input()
cc = set('(',')')
ans = []
# tmp = dict()
# tmp['('] = 0
# tmp[')'] = 0


id = 0
flg = 0
tmp = []
while(id != n):

    if S[id] == '(':
        tmp.add(S[id])
        
print(''.join(ans))