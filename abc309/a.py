A,B = map(int,input().split())

map = [[1,2,3],[4,5,6],[7,8,9]]

# for i in map:
#     if (A in map) and (B in map):
#         if B == A+1:
#             print('Yes')
#             exit()
# print('No')

if (A == 1 and B == 2) or (A == 4 and B == 5) or (A == 7 and B == 8) or (A == 2 and B == 3) or (A == 5 and B == 6) or (A == 8 and B == 9):
    print('Yes')
else:
    print('No')