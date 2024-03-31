s = input()
S = [ord(i) for i in s]
mid_S = s[2:-1]
M = [ord(i) for i in mid_S]
A = 65
C = 67
a = 97
z = 122

if S[0] == A:
    if C in M:
        S = S[1:]
        S.remove(C)

        if len([i for i in S if a<=i<=z]) == (len(s)-2):
            print('AC')
            exit()

print('WA')


