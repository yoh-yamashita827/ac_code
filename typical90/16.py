N = int(input())
A,B,C = map(int,input().split())

'''
Ax + By + Cz = N
を考えると，(x,y,z)の数を求めたら良い．
zの最大値を考えると N//c
yの最大値は (N-Cz)//b
xの最大値は (N-Cz-By)//a
であるため，最大値から探索していけばいいね！

x+y+z <= 9999
だからx,yについての2重ループを考えると1e08程度に収まる

'''

for x in range(1,10000):
    for y in range(1,10000):
        if (((A*x)+(B*y))%C != 0) or x+y > 9999:
            continue
        z = N-(((A*x)+(B*y))%C)

