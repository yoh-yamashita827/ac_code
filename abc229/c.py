#　入力受け取り
N,W = map(int,input().split())     #　数字　空白　数字　で入力すると　Nに左の数字、Wに右の数字が入る
l = [list(map(int,input().split())) for i in range(N)]#　おいしさAと重さBをセットでリストにする　[[A1,B1][A2,B2][A3,B3]...]

#　変数準備
wei = 0         #　乗せたチーズの重さの合計
worth = 0       #  乗せたチーズの美味しさの合計
l_sort = sorted(l, reverse = True)     # チーズの美味しさが大きい順に並べ替える

#　実行部分
for i in range(N):          #　N回ループを回す
    cnt = l_sort[i][1]      #　ソートしたリストのi番目の右　i番目に美味しいチーズの重さをcntとする
    if W - wei < cnt:       #  もし規定の重さWと現在のチーズの重さweiとの差がcntより小さかったら残りの重さ分だけチーズを追加してbreak
        cnt = W - wei
        worth += cnt * l_sort[i][0]
        break
    wei += l_sort[i][1]     # まだ規定の重さに達しない場合、i番目に美味しいチーズをその重さ分追加する
    worth += l_sort[i][1] * l_sort[i][0]

print(worth)
