n = int(input())
item = ['(',')']

from collections import deque


for i in range(1,2**n):
    ans = ''
    stack = deque()
    bit_n = bin(i).split('0b')[-1].zfill(n)

    for j in bit_n:
        if j == '0':
            ans += item[int(j)]
            stack.append(item[int(j)])
        else:

            if len(stack) == 0:
                break
            else:
                stack.pop()
                ans += item[int(j)]

    if (len(ans) ==  n) and (len(stack) == 0):
        print(ans)
    else:
        continue





