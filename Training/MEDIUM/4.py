s=input()

if len(s)%2!=0:
    s = s[:-1]
else:
    s = s[:-2]
while(s!=''):
    if s[:(len(s)//2)]== s[(len(s)//2):]:
        print((len(s)))
        exit()
    s = s[:-2]

print(0)