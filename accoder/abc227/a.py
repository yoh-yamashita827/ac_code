a, b, c = map(int, input().split())

for i in range(b-1):
    if  a == c:
        c = 1
    else:
        c += 1

print(c)