import math
def main(lines):
    for i,v in enumerate(lines):
        if i == 0:
            n,m,T = map(int,v.split())
            cost = [[0]*n for _ in range(n)] 
        else:
            u,v,w = map(int,v.split())
            cost[u-1][v-1] = w   # 扱いやすいように0インデックスに直す

    visited = dict()
    point = 0
    for t in range(T):
        if point in visited.keys():
           break   
        visited[point] = t      
        curry = max(range(len(cost[point])), key=cost[point].__getitem__) # argmax(numpy使わないver)
        if cost[curry] == [0]*n:  # 0が帰ってきたら，道はないので留まる
            print(point+1)
            return 0
        point = curry

    ##　ここにきた時点で，サイクルが発見された状態．
    cycle_len = max(visited.values())-visited[point]+1
    untill = visited[point]  # サイクルに到達するのにかかる時間
    cycle_t = (((T-untill+(cycle_len-1))%(cycle_len)))+1 # サイクルの間をどこまでいけるか
    last_point = [k for k, v in visited.items() if v == (untill+cycle_t)] # 最終的な位置を計算
    print(last_point[0]+1)
    

if __name__ == '__main__':
    lines = ['5 5 4','5 2 5','2 3 4','3 5 3','3 4 2','1 3 1']
    # lines = ['3 3 4','1 2 1','2 3 3','3 1 2']
    main(lines)