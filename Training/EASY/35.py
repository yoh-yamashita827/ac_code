s = list(input())
if len(set(s)) == 26:
    print('None')
    exit()

s.sort()

ss = [ord(i) for i in s]

for i in range(97,123):
    if i not in ss:
        print(chr(i))
        break