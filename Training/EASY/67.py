n = int(input())
names = {}
for _ in range(n):
    s = input()

    if s not in names.keys():
        names[s] = 1
    else:
        names[s] += 1
max_cnt = max(names.values())
max_names = [i for i,v in names.items() if v == max_cnt]
# max_names = []
# for i,v in names.items():
#     if v == max() 
max_names.sort()

for i in max_names:
    print(i)