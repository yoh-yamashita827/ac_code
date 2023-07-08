import string
S = list(input())
T = list(input())

a = (list(string.ascii_lowercase))
b = (ord(T[0]) - ord(S[0]))

for i in range(len(S)):

    if T[i] != chr((ord(S[i])+b)%26):
        print((ord(S[i])+b)%95,S[i])
        print('No')
        exit(0)

 

print('Yes')

