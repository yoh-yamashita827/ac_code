N = int(input('何ベン図問題？'))

if N == 2:
    print('既知の情報を教えてください,未知の値は0としてください')
    total = int(input('合計人数'))
    a = int(input('Aの人数'))
    b = int(input('Bの人数'))
    ab = int(input('AとBの両方の人数'))
    only_a = int(input('Aだけの人数'))
    only_b = int(input('Bだけの人数'))
    other = int(input('AでもBでもない人数'))

    w = a+b-total
    