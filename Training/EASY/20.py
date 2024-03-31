s=int(input())
ans = set()
id = 0

while(1):
    if s in ans:
        print(id+1)
        break
    ans.add(s)
    if s%2 == 0:
        s = s//2
    else:
        s = (3*s)+1
    id += 1