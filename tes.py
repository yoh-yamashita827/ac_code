n,k = map(int,input().split())

def divisors_list_s(num):
   divisors = 0
   for i in range(1, int(num**0.5)+1):
       if num % i == 0:
           divisors+=2 
           if i**2 == num:
               divisors-=1

   return divisors # 昇順にしなくてよいならソートは不要

ans = 0
for x in range(int(k**(1/2))+1):
    ans+=(divisors_list_s(x))

print(x)
