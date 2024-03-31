# n = int(input())
n,m = map(int,input().split())
s = input()
t = input()
# c = list(map(int,input().split()))
# s = []
# for _ in range(n):
#     s.append(input())

if (t[:n] == s) and (t[-n:] == s):
    print(0)
elif (t[:n] == s):
    print(1)
elif (t[-n:] == s):
    print(2)
else:
    print(3)