n = int(input())
t = list(map(int,input().split()))

ans = [i for i in t if i % 2 == 0]
print(*ans)