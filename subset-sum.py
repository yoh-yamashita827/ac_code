import time
import random
import numpy as np
N = int(input("N:"))
p = random.sample(range(1,16),k=N)
print(p)
# p = [4,7,3,2,6,5,2,3,5,9]
W = int(input("W:"))

def subset_bit(W,value):
    subset = 0
    for i in range(1,2**N):
        weight_i = []
        bit_n = bin(i).split('0b')[-1].zfill(N)

        for ind,j in enumerate(bit_n):
            if j == '1':
                weight_i.append(value[ind])

        if (sum(weight_i) <= W):
            subset += 1
        else:
            continue
    return subset

def subset_dp(n,W):
    M = [[0]*(W+1) for _ in range(len(n)+1)]
    for i in range(1,len(n)):
        for j in range(0,W+1):
            if j < n[i-1]:
                M[i][j] = M[i-1][j]
            else:
                M[i][j] = max(M[i-1][j],n[i-1]+ M[i-1][j-n[i-1]])
    # print(np.array(M))
    return M[-1][-1]




tm1 = 0
for _ in range(5):
    start = time.time()
    ans = subset_bit(W,p)
    time1 = time.time()-start
    tm1 += time1

print("bit",tm1/5)

tm2 = 0
for _ in range(5):
    start = time.time()
    ans = subset_dp(p,W)
    time2 = time.time()-start
    tm2 += time2

print("dp",tm2/5)

print("理論値",(((2**N)/W)))
print("実測値",(tm1/tm2))







