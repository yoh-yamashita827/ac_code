def main():
    from heapq import heappush, heappop

    n, m ,k= map(int, input().split())

    graph = [[] for _ in range(n)]

    for _ in range(m):
        u, v, c = map(int, input().split())

        graph[u-1].append((v-1, c%k)) # u->vの辺
        graph[v-1].append((u-1, c%k)) # v->uの辺

    # プリム法
    # 頂点がマークされているか確認する配列
    marked = [False for _ in range(n)]

    # マークされている頂点数を数える
    marked_cnt = 0

    # はじめに0頂点をマーク
    marked[0] = True
    marked_cnt += 1

    # heap
    q = []

    # 頂点0に隣接する辺を保存
    for j, c in graph[0]:
        heappush(q, (c, j))

    total = 0

    # すべての頂点をマークするまでwhileループ
    while marked_cnt < n:
        # 最小の重みの辺をheapで取り出す
        c, i = heappop(q)

        # マークされているならスキップ
        if marked[i]:
            continue

        # 頂点をマーク
        marked[i] = True
        marked_cnt += 1

        total += c

        # 頂点iに隣接する辺を保存
        for j, c in graph[i]:
            # マークされていればスキップ
            if marked[j]:
                continue

            heappush(q, (c, j))

    print(total%k)


if __name__ == '__main__':
    main()
