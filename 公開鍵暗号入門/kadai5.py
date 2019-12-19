import matplotlib.pyplot as plt
import time
import random
from math import sqrt
import numpy as np


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
def fermat_test(p):
    # p=0,1の場合素数ではない。
    if p < 2:
        return 0
    k = 0  # Temporary変数（LOOP用）
    s = p/10  # ループ繰り返し回数

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


error = 0  # 誤差数
# カーマイケル数
carmichael = [561, 1105, 1729, 2465,
              2821, 6601, 8911, 10585,
              15841, 29341, 41041, 46657,
              52633, 62745, 63973, 75361]

variable = 3000  # どこまで素数を調べるか指定

for i in range(variable):
    if i in carmichael:
        continue
    result = fermat_test(i)  # Fermatテストの結果
    prime = prime_number(i)  # 素数かどうか確認
    if result != prime:
        error += 1  # 結果が誤っていたら誤差数を増やす

print("誤差率：", error/variable)