'''
S = 0_________1
2 <= N <= 2*10^5

?i <--- 1 <= i <= N
return Si
'''
N = int(input())
def QA(i):
    print('?',i)
    return int(input())

def Ans(i):
    print('!',i)
    exit()

l = 1
r = N
p = 0
while(True):
    m = (l+r)//2
    Sm = QA(m)

    if Sm == 0:
        l = m
    else:
        r = m
    
    if l+1 == r:
        p = l
        break
Ans(p)


# id = 0
# s = QA(id+2)
# while(id <= 19):
#     id += 1
#     if QA(id+2) == 0:
#         continue
#     else:
#         Ans(id+1)
#         break





    

