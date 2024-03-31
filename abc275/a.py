n = int(input())
# n,m = map(int,input().split())
# s = input()
h = list(map(int,input().split()))
# s = []
# for _ in range(n):
#    s.append(input())


print(h.index(max(h))+1)