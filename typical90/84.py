N = int(input())
S = input()
ans = 0
left = 0

for i, s in enumerate(S):
    if S[left] != s: # 現在の文字と前の文字が異なる場合
        ans += (i - left) * (N - i) # 条件を満たす整数の組を加算 (区間の長さ * その区間以降の文字数)
        left = i
print(ans)