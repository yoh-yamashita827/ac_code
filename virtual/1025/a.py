# n = int(input())
p,q = map(str,input().split())
# s = input()
# c = list(map(int,input().split()))
# s = []
# for _ in range(n):
#     s.append(input())

dist = [0,3,1,4,1,5,9]
mt = [sum(dist[:i+1]) for i in range(len(dist))]

# print(mt)
l = ord(p)%65
r = ord(q)%65
# print(l,r)
print(abs(mt[r]-mt[l]))