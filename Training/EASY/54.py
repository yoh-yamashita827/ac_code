n = int(input())
w = [input() for _ in range(n)]

said = set()
shiri = w[0][0]

for i in w:
    if i not in said:
        said.add(i)
        if shiri != i[0]:
            print('No')
            exit()
        shiri = i[-1]

    else:
        print('No')
        exit()
print('Yes')