import math
N = int(input())

n2 = [0]+[2**i for i in range(9)]

for i in range(len(n2)):
    if n2[i] > N:
        print(n2[i-1])
        exit()
