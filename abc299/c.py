N = int(input())
S = list(input())
ans = -1
flg = False
import itertools
for key,g in itertools.groupby(S):
    gru = list(g)
    if key == 'o' and ans < len(gru):
        ans = len(gru)
    if key == '-':
        flg = True
        
if flg:
    print(ans)
else:
    print(-1)
# inds = [i for i, x in enumerate(S) if x == '-']
# if inds == []:
#     print(ans)
#     exit()

# if len(inds) == 1:
#     if len(S) == 1:
#         print(-1)
#         exit()
#     ans= (max(inds[0],N-inds[0]))cd ..

#     print(ans-1)
#     exit()

# tmp = inds.copy()
# tmp.pop(-1)
# tmp = [0] + tmp
# length = [x-y for (x,y) in zip(inds,tmp)]
# print(max(length)-1)