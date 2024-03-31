s = input()
t = input()

for i in range(len(s)):
    if s == t:
        print('Yes')
        exit()
        
    s = s[1:]+s[0]


print('No')