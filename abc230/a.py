N = int(input())

if N > 41:
    N += 1

num_zero = str(N).zfill(3)

print('AGC'+num_zero)