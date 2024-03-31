n,k = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
# A.sort()
# B.sort()
cnt = 0
for i,j in zip(A,B):
    cnt += abs(i-j)

# if (cnt%2)==(k%2):
#     if cnt <= k:
#         print('Yes')
#         exit()
# print('No')

if cnt > k:
    print('No')
    exit()
if (cnt%2) != (k%2):
    print('No')
    exit()

print('Yes')