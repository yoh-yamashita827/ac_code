import itertools
s=input()
atcg = ['A','T','C','G']
ss = ['0' if i in atcg else i for i in s]

ans = 0
for i in range(10):
    for j in range(i,11):
        if i==j:continue
        window = ss[i:j]
        if {'0'} == set(list(window)):
            ans = max(ans,len(window))


print(ans)