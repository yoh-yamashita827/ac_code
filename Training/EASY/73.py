s = input()

ss = [int(i) for i in s[1:]]
ans = 0
S = ''
for i in ss:
    if i != 9:
        ans += 9
        S = '9'
    else:
        ans += 8
        S = '8'
print(ans+int(s[0])-1)