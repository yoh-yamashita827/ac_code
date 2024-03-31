o = input()
e = input()

ans = ''



for i,j in zip(o,e):
    ans += i
    ans += j

if len(o) == len(e):
    print(ans)
elif len(o) > len(e):
    print(ans+o[-1])
else:
    print(ans+e[-1])