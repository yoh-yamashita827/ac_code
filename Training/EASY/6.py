h,w=map(int,input().split())
if (h==1)or(w==1):
    print(1)
elif h%2 != 0:
    print(w*(h//2)+(w+1)//2)
else:
    print(w*(h//2))