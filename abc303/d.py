x,y,z = map(int,input().split())
s = input()

capslock = False

def nyakki(left,right,alt = False):
    now = s[left]

    if alt:
        for i in range(left+1,right-1):
            if now == s[i]:
                break

        return i-1
    
    else:
        for i in range(left+1,right-1):
            if now != s[i]:
                break

        return i-1
    
cnt_x,cnt_y,cnt_z = 0  
while(1):
    start = s[0]
    next = s[1]

    if start == next:
        roop = 0
        if start == 'a':
            if (2*x) >= (z+2*y):
                cnt_z += 1
            roop += 1
        