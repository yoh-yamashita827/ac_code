a,b,c = map(int,input().split())
flg = False
flg2 =False

if c % 2 == 0:
    flg = True


if flg:
    if  abs(a) == abs(b):
        print("=")
    elif abs(a) < abs(b):
        print("<")
    else:
        print(">")

else:
    if a < b:
        print("<")
    elif a == b :
        print("=")
    else:
        print(">")
