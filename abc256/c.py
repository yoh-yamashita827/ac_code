# n = int(input())
h1,h2,h3,m1,m2,m3 = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
# s = []
# for _ in range(n):
#     s.append(input())

cnt = 0
for a in range(1,31):
    for b in range(1,31):
        for d in range(1,31):
            for e in range(1,31):

                c = h1-(a+b)
                f = h2-(d+e)
                g = m1-(a+d)
                h = m2-(b+e)
                i = m3-(c+f)
                # i2 = h3-(g+h)

                # if (g+h+i == h3) and (c*f*g*h*i > 0) :
                if (g+h+i == h3) and (min([c,f,g,h,i]) > 0) :
                    cnt+= 1

print(cnt)