p,q = map(str,input().split())

l = ord(p)%65
r = ord(q)%65

if l > r:
    l,r = r,l

dis = [3,1,4,1,5,9]
ans = 0
while(l!=r):
    ans += dis[l]
    l+=1
print(ans)