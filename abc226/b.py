N = int(input())
l = [list(map(int, input().split())) for l in range(N)]

l = list(map(list, set(map(tuple, l))))

print(len(l))