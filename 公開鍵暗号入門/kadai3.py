def modInverse(N, a):
    N0 = N
    y = 0
    x = 1

    if N == 1:
        return 0

    while a > 1:
        q = int(a / N)
        t = N

        # m は現在余り
        # ユークリッドアルゴ
        N = a % N
        a = t
        t = y

        # y と xを更新
        y = x - (q * y)
        x = t

    # 求めたxが負の数であれば正にする
    if x < 0:
        x = x + N0

    return x


p = 101
q = 107
N = p*q
e = 3

# 平文のメッセージ
m = list(range(0,N-1))
print("メッセージ（平文）:", m)

C = []  # 暗号文
m_new = []  # 復号化された平文

# 秘密鍵を計算する
d = modInverse((p-1)*(q-1),3)

# C 暗号文を求める
for i in range(0, N-1):
    C.append(pow(m[i], 3) % N)
print("暗号化後: ", C)

# 復号化する
for i in range(0, N-1):
    m_new.append(pow(C[i],d) % N)
print("復号化後：", m_new)

