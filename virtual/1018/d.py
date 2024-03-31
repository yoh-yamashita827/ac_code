k = int(input())
# n,m = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
# s = []
# for _ in range(n):
#     s.append(input())

k_2 = bin(k)[2:]

ans = ''

for i in k_2:
    if i == '1':
        ans += '2'

    else:
        ans += i


print(ans)


