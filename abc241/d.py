q = int(input())
a = []
l = []
s = []
p = []
cnt1 = 0
cnt2 = 0

for i in range(q):
    a = map(str,input().split())
    if a[0] == '1':
        l.append(int(a[1]))
        s = sorted(l,reverse=True)
        p = sorted(l)

    elif a[0] == 2:
        for i in range(5):
            if s[i] >= a[1]:
                cnt1 += 1
                if cnt1 == a[2]:
                    print(s[i])

    else:
        for i in range(5):
            if s[i] <= a[1]:
                cnt2 += 1
                if cnt2 == a[2]:
                    print(s[i])



