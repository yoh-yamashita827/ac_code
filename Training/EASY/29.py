s=input()

import itertools
ans = 753
for i in range(len(s)-2):
    num = s[i:i+3]
    ans = min(ans,abs(753-int(num)))

print(ans)