def prime_number(x):
    for i in range(x,100004):
        j = 2
        flg = False
        while(j < int(x**(1/2))+1):
            if i%j == 0:
                flg = True
                break
            j += 1
        if not flg:
            return i
        
x = int(input())
print(prime_number(x))