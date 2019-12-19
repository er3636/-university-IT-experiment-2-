
while True:
    print("法とする数字:")
    N = int(input())
    print("逆元を求める数字:")
    a = int(input())

    if a <= 0 or N <= 0:
        print("入力が誤っています。再度入力してください")
    else:
        break

def modInverse(N, a):
    N0 = N
    y = 0
    x = 1

    if N == 1:
        return 0

    while a > 1:
        q = int(a / N)
        t = N

        # N は現在余り
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


print("逆元:", modInverse(N, a))
