n = int(input())

def throw(num):
    tmp = str(num)
    n = len(tmp)
    ans = tmp[0:3]

    return (''.join(ans)).ljust(n,'0')

# if n <= 1000-1:
#     print(n)

# elif n <= 10000-1:
#     print()

print(throw(n))


