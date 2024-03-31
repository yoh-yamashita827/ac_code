n = int(input())
class Gozyo:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def gcd(a, b):
        if b == 0:
            return a
        else:
            return Gozyo.gcd(b, a % b)

    def lcm(self):
        return int(self.a * self.b // Gozyo.gcd(self.a, self.b))
    
ans = ''
import math
for i in range(n+1):
    if i == 0:
        ans += '1'
        continue
    # judge = Gozyo(n,i)

    # tmp = judge.lcm()
    tmp = math.gcd(n,i)

    if 1 <= n//tmp <= 9:
        ans += str(n//tmp)
    else:ans += '-'

print(ans)