n,m = map(int,input().split())
foods = set(list(range(1,m+1)))


for i in range(n):
    anke = list(map(int,input().split()))
    k = anke.pop(0)

    foods &= set(anke)

print(len(foods))