# n = int(input())
# n,m = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
s = [input() for _ in range(10)]
# for _ in range(n):
#     s.append(input())
a=b=c=d= 0
for ii,i in enumerate(s):
    if '#' in i:
        if c == 0:
            c = ii+1
        
        a = i.find('#')+1
        b = i.rfind('#')+1
        d = ii+1

print(c,d)
print(a,b)
