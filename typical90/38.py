a,b = map(int,input().split())

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

    

ans = Gozyo(a,b).lcm()
if ans > 10**18:
    print('Large')
    
else:print(ans)
        
