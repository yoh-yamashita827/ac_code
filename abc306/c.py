N = int(input())
A = list(map(int,input().split()))
# from collections import defaultdict
# num_dict = defaultdict()
num_dict = {(i): A[i] for i in range(0, len(A))}
# num_dict = {}

num = set()

for key,v in list(num_dict.items()):
    if v not in num:
        num.add(v)
        del num_dict[key]
        # num_dict.pop(key)

num = set()
for key,v in reversed(list(num_dict.items())):
    if v not in num:
        num.add(v)
        del num_dict[key]

print(*list(num_dict.values()))
