import math
def main(lines):
    for i,v in enumerate(lines):
        if i == 0:
            N = int(v)
        elif i == 1:
            K = int(v)
        else:
            A = list(map(int,v.split()))

    ans = 0
    for i in A:
        dev = math.log(i,K)  # iがKの何乗かを計算する
        ans += int(dev)  # この整数部分がKで割り切れる回数

    print(ans)

if __name__ == '__main__':
    lines = ['5','10','100000 100000 100000 100000 100000']
    main(lines)