n = int(input())
aa = [int(input()) for _ in range(n)]

# for i in range(n):
#     l = a[:i]
#     r = a[i+1:]

#     if (l==[]):
#         print(max(0,max(r)))
#     elif (r==[]):
#         print(max(max(l),0))
#     else:
#         print(max(max(l),max(r)))
a = sorted(aa)
top1 = a[-1]
top2 = a[-2]

for i in aa:
    if i == top1:
        print(top2)
    else:
        print(top1)