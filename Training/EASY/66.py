s = input()

if (s.count('N') and s.count('S')):
    if (s.count('E')  and s.count('W')):
        print('Yes')
        exit()

if (s.count('N') and s.count('S')):
    if not (s.count('E') or s.count('W')):    
        print('Yes')
        exit()

if (s.count('E') and s.count('W')):
    if (s.count('N')  and s.count('S')):
        print('Yes')
        exit()

if (s.count('E') and s.count('W')):
    if not (s.count('N') or s.count('S')):    
        print('Yes')
        exit()
print('No') 