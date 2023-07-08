s = input()
s_min = s
s_max = s
shift = s

def left(s_list):
    tmp = s_list.pop(0)
    return s_list.append(tmp)

def right(s_list):
    tmp = list(s_list.pop())
    return tmp+s_list

for i in range(len(s)):
    shift = ''.join(right(list(shift)))

    if s_min > shift:
        s_min = shift

    if s_max < shift:
        s_max = shift

print(s_min)
print(s_max)
