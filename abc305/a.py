n = 2*int(input())

def my_round(val, digit=0):
    p = 10 ** digit
    return (val * p * 2 + 1) // 2 / p

print(int((my_round(n,-1))/2))