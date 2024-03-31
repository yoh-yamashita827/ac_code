x = int(input())

if x < 100:
    print(0)
    exit()

if x%100 > 5*(x//100):
    print(0)
    exit()

print(1)