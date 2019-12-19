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
    flag = 0  # 候補が判定されたかどうかをチェックするフラグ
    candidate = 0  # 候補
    K = 3*length**2  # 最大繰り返し数
    i = 1  # 繰り返し変数
    # STEP-1: 整数をランダムに選ぶ
    while flag == 0 and i <= K:
        bits = ["0", "1"]
        number = ""
        for j in range(length - 1):  # n-1ビットの2進数整数をランダムに選ぶ
            number = number + bits[random.randint(0, 1)]
        # STEP-2: 選んだ整数の先頭に「1」を付け加えて候補にする
        number = "1" + number
        candidate = int(number, 2)  # 10進数にする
        # 素数かどうかを判定する、判定されれば終了
        flag = fermat_test(candidate)
        i += 1
    return candidate


for i in range(2, 16):
    print(i, "bit prime number: ", create_prime_number(i))
