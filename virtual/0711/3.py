X,A,B = map(int,input().split())

date = B-A

if date <= 0:
    print('delicious')
elif date <= X:
    print('safe')
else:
    print('dangerous ')