N = int(input())
H = list(map(int,input().split()))


l = 0
r = 1
length = []
pre = H[0]

while(r < N):
    if H[r] <= pre:
        pre = H[r]
        r += 1
        
    else:
        length.append(r-l-1)
        l = r
        r = l+1
        pre = H[l]

length.append(r-l-1)
print(length)
print(max(length))