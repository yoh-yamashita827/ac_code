n = int(input())
X = list(map(int,input().split()))

X.sort()

score = X[n:-n]

print((sum(score))/(len(score)))

