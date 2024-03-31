h,w=map(int,input().split())
s=[list(input()) for _ in range(h)]
walk=[
    (1,0),
    (-1,0),
    (0,1),
    (0,-1),
    (1,1),
    (1,-1),
    (-1,1),
    (-1,-1),
]

for i in range(h):
    for j in range(w):
        if s[i][j] == '.':
            s[i][j] = 0

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            for xy in walk:
                x = xy[0]
                y = xy[1]
                if (0 <= j+x < w) and (0 <= i+y < h) and (s[i+y][j+x] != '#'):
                    s[i+y][j+x] += 1

for ans in [[str(s[i][j]) for j in range(w)] for i in range(h)]:
    print(''.join(ans))