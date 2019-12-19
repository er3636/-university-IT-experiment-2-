import random

# 最大公約数
def gcd(a, b):
    if a < b:
        a, b = b, a

    # ユークリッドの互除法
    while b:
        q = int(a / b)
        remainder = a % b
        a = b
        b = remainder
    return a


# 素数判定
def fermat_test(p):
    # p=0,1の場合素数ではない。
    if p < 2:
        return 0
    k = 0  # Temporary変数（LOOP用）
    s = p/3  # ループ繰り返し回数

    # テスト開始
    while k < s:
        a = random.randint(1, p - 1)  # ランダム数
        if gcd(a, p) != 1:
            return 0
        if (pow(a, p-1) % p) != 1:
            return 0
        k = k + 1
    # 素数でないと確認できなかったら素数と判断
    return 1


def create_prime_number(length):
    flag = 0
    candidate = 0
    K = 3*length**2
    i = 1
    # STEP-1: 整数をランダムに選ぶ
    while flag == 0 and i <= K:
        bits = ["0", "1"]
        number = ""
        for j in range(length - 1):
            number = number + bits[random.randint(0, 1)]
        # STEP-2: 選んだ整数の先頭に「1」を付け加えて候補にする
        number = "1" + number
        candidate = int(number, 2)
        # 素数かどうかを判定する、判定されれば終了
        flag = fermat_test(candidate)
        i += 1
    return candidate


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


p = create_prime_number(7)
q = create_prime_number(8)

A = p*q
e = 3

# 平文のメッセージ
m = list(range(0, A-1))
print("メッセージ（平文）:", m)

C = []  # 暗号文
m_new = []  # 復号化された平文

# 秘密鍵を計算する
d = modInverse((p-1)*(q-1), 3)

# C 暗号文を求める
for i in range(0, A-1):
    C.append(pow(m[i], 3) % A)
print("暗号化後: ", C)

# 復号化する
for i in range(0, A-1):
    m_new.append(pow(C[i],d) % A)
print("復号化後：", m_new)
