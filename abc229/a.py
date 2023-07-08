s1 = list(input())
s2 = list(input())


if (s1[0] == s1[1] == '#') or (s2[0] == s2[1] == '#') or (s1[0] == s2[0] == '#') or (s1[1] == s2[1] == '#'):
    print('Yes')

else:
    print('No')