import math
N = int(input())
B_max = int(math.sqrt(N))
A_max = int(math.sqrt(B_max))
cnt = 0
cnt2 = 0

for i in range(1,B_max+1):
    cnt += N/i
    cnt2 += i-1

cnt3 = 2*(A_max - 1)

print(int(cnt-cnt2))
