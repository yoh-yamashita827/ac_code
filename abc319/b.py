n = int(input())
# n,m = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
# s = []
# for _ in range(n):
#    s.append(input())


def divisor(n):
    ans = []
    for i in range(1,10):
        if n%i == 0:
            ans.append(i)

    return ans
def judge(i,j):
    if i == 0:
        return str(1)
    
    if n%j == 0:
        if i <= (n//j):
            if (n//j)%i == 0:
                return str(j)
            
    return 0
ans = ''
nums = divisor(n)
for i in range(n):
    flg = False
    for j in nums:
        tmp = judge(i,j)
        if tmp:
            ans += str(tmp)
            break
        else:
            ans += '-'
            break

    

print(ans)
