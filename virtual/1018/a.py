# n = int(input())
# n,m = map(int,input().split())
# s = input()
# c = list(map(int,input().split()))
# s = []
# for _ in range(n):
#     s.append(input())
atc = ['ABC' , 'ARC' , 'AGC' , 'AHC']
# flg = [False*4]
s = [input() for _ in range(3)]

for i in s:
    atc.remove(i)

print(atc[0])
