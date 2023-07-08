
'''
a < b < c なる整数で, N <= a*a*b*c*c
を満たす個数を数えろ 
-------------------------------------
N_max = 10^12
N_maxの5乗根を考えると,約251
2~251まで素数を生成し,3重ループで評価すれば良いはず
だめめめえめ

N_maxの5乗根はN_maxを作る最小値とも考えれる.
実際はa=2,b=3の時にとりえる最大素数までを探索しなければならない.
つまり,考えるのは288675まで
'''
N = int(input())

def prime(limit):
    prime = []
    for i in range(2, limit+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime.append(i)
    return prime

pr_list = prime(288653)
cnt = 0
for i in range(len(pr_list)):
    for j in range(i,len(pr_list)):
        for k in range(j,len(pr_list)):
            if not (i < j < k):
                continue
            else:
                a,b,c = pr_list[i],pr_list[j],pr_list[k]
                if a**2*b*c**2 <= N:
                    cnt += 1
print(cnt)
            


