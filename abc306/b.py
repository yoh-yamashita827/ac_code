A = list(map(str,input().split()))

B = A[::-1]

bit = '0b'+''.join(B)

print(int(bit,2))