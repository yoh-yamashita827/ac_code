n,a,b = map(int,input().split())
s=input()
cnt_a = 0
cnt_b = 0
for i in s:
    if i == 'a':
        if (cnt_a+cnt_b) < a+b:
            print('Yes')
            cnt_a += 1
        else:
            print('No')

    elif i == 'b':
        if (cnt_a+cnt_b) < a+b:
            if cnt_b < b:
                print('Yes')
                cnt_b += 1
            else:
                print('No')
        else:
            print('No')
    else:
        print('No')