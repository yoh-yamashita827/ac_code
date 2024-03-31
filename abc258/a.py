k = int(input())
# n,m = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
# s = []
# for _ in range(n):
#    s.append(input())

def seikei(x):
    if x < 10:
        return '0'+str(x)
    else:
        return str(x)
    
m = seikei(k%60)

if k >= 60:
    print('22:'+str(m))
else:
    print('21:'+str(m))