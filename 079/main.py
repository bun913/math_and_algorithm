"""
i番目の整数Aiについてi%Aiを足し合わせていき最大値を求める
全探索では間に合わないので、傾向を掴むために全探索で最大値を求める
すると以下のような性質がある
N: Miの合計とする
1: 0
2: 1
3: 3
4: 6
5: 10
6: 15
これをよく見るとMiはi-1の時の数列の合計値となっていることがわかる
これを和の公式に当てはめてみると、1/2n(n-1)となることがわかる
→和の公式  (初項 + 末項) * 項数 / 2 をn-1に当てはめるとそうなる
"""
N = int(input())
ans = N * (N-1) // 2
print(ans)