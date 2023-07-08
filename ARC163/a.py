T = int(input())

# for i in range(T):
#     n = int(input())
#     s = input()
#     flg = True
#     sp = []
#     for i in range(n-1):
#         now = s[i]
#         next = s[i+1]

#         if now > next:
#             sp.append(i+1)

#     sp = [0]+sp
#     sp.append(n)
#     pre = s[sp[0]:sp[1]]
#     for t in range(1,len(sp)-1):
#         ttt = s[sp[t]:sp[t+1]]

#         if pre > ttt:
#             flg = False

#     if flg:
#         print('Yes')
#     else:
#         print('No')
for i in range(T):
    n = int(input())
    s = input()
    flg = False

    for i in range(n):
        if s[0:i+1] < s[i+1:]:
            flg = True


    if flg:
        print('Yes')
    else:
        print('No')