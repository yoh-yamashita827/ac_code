a,b = map(int,input().split())

def swap(a,b):
    if a < b:
        a,b = b,a
    return a,b
a,b = swap(a,b)
cnt = 0

while(1):
    if b == 0:
        break
    s = a-b

    if s == 0:
        break

    n = a//s

    cnt += n
    
    b = a-(n*s)
    a = s
    print(a,b)
    
if cnt <= 0:
    print(0)
else:
    print(cnt-1)


