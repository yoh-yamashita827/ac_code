n = int(input())
exist = set()
day = 1
for i in range(n):
    s = input()
    if s not in exist:
        print(day)
    exist.add(s)
    day += 1
