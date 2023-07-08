N = int(input())
S = str(input())

s = S.find('|')
e = S.rfind('|')
ast = S.find('*')
if s < ast < e:
    print('in')
else:
    print('out')
