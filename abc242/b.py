s = input()
s_lis = list(s)
num = []
min = 0


for i in range(len(s)):
    num.append(ord(s_lis[i]))

    

num.sort()


for i in range(len(s)):
    num[i] = chr(num[i])
    

min = ''.join(num)
print(min)