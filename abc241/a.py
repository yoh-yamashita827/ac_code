a = list(map(int,input().split()))
num = a[0]

for i in range(2):
    num = a[num]

print(num)
