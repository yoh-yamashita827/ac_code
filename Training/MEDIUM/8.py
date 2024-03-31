n = int(input())
a = list(map(int,input().split()))

def color_code(rate):
    for i in range(8):
        if (i*400) <= rate <=(i*400)+399:
            return i
    return -1
colors = set()
red = 0
for i in a:
    color = color_code(i)
    if color == -1:
        red += 1
    else:
        colors.add(color)

    
print(max(1,len(colors)),((len(colors)+red)))