# n = int(input())
n,m = map(int,input().split())
# s = input()
A = list(map(int,input().split()))
# s = [input() for _  in range(n)]

x = [i for i in A if i>=m]
print(len(x))
