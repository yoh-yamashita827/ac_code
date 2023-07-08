a,b = map(int,input().split())
cnt = 0
def swap(a,b):
    if a < b:
        a,b = b,a
    return a,b

a,b = swap(a,b)

while(b>0):
    cnt += a//b
    a = a%b
    a,b = swap(a,b)
    print(a,b)

print(cnt-1)

