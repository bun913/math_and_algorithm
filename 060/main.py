"""
実際に規則性を考えてみる
Nが3以下の時は先手が絶対勝つ
Nが4の時は後手が絶対勝つ
Nが5の時は先手が絶対勝つ
と繰り返していくと残4の状態を先に持った方が負ける
"""

N = int(input())
if N <= 3:
    print('First')
    exit()
if N % 4 == 0:
    print('Second')
    exit()
print('First')