import matplotlib.pyplot as plt
import time
import random
from math import sqrt, log2
import numpy as np


def prime_number(number):
    flag = 0  # numberが素数である場合は flag=0 のままである
    if number == 0 or number == 1:  # numberは0か1の時は調べない
        return 0
    # 2からルート(number)までが割り切れるかどうか調べる
    for j in range(2, int(sqrt(number))+1):
        # 割り切れれば flag=1 (素数ではない)
        if number % j == 0:
            flag = 1
            break
    if flag != 1:
        return 1
    else:
        return 0


# 素数判定
def miller_rabin(p):
    # p=0,1の場合素数ではない。
    if p < 2:
        return 0
    # p>2 かつ偶数であれば「素数ではない」
    if p > 2 and p % 2 == 0:
        return 0

    k = 0  # Temporary変数（LOOP用）
    s = 10  # ループ繰り返し回数

    # vとuの計算（u=0, v=p-1で初期値を設定）
    u = 0
    v = p - 1
    # p-1（つまりv）が2で割り切れなくなるまで2で割る
    # 割れた回数がu, 最後に割り切れない時のvが目的のvとなっている
    while v % 2 == 0:
        v = v / 2
        u += 1
    v = int(v)

    # テスト開始
    while k < s:
        a = random.randint(1, p - 1)  # ランダム数
        if (pow(a, p-1) % p) != 1:
            return 0
        for j in range(u+1):
            m = n = a % p
            #pow(a, pow(2, j))が非常に大きい数字になってしまうため、gcd(p, pow(a, pow(2, j)))=1という特徴を使う
            # つまりあまりの乗を求める
            for i in range(2, pow(2, j)*v + 1):
                m = m * (a % p)
                m = m % p
            for i in range(2, int(pow(2, j-1)*v) + 1):
                n = n * (a % p)
                n = n % p
            if m == 1 and (n == 1 or (n == p-1)):
                return 0

        k = k + 1
    # 素数でないと確認できなかったら素数と判断
    return 1

error = 0  # 誤差数
# カーマイケル数
carmichael = [561, 1105, 1729, 2465, 2821, 6601, 8911,
              10585, 15841, 29341, 41041, 46657, 52633,
              62745, 63973, 75361, 101101, 115921, 126217,
              162401, 172081, 188461, 252601, 278545,
              294409, 314821, 334153, 340561, 399001,
              410041, 449065, 488881, 512461]

for i in carmichael:
    result = miller_rabin(i)  # Miller-Rabinテストの結果
    prime = prime_number(i)  # 素数かどうか確認
    if result != prime:
        error += 1  # 結果が誤っていたら誤差数を増やす

print(error/len(carmichael))
