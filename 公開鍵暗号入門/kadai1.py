
while True:
    print("2つの自然数を入力してください")
    a = int(input())
    b = int(input())
    if a <= 0 or b <= 0:
        print("入力が誤っています。再度入力してください")
    else:
        break

# 大きい方をa,小さい方をbとする。
if a < b:
    a, b = b, a

#ユークリッドの互除法
while b:
    q = int(a / b)
    remainder = a % b
    a = b
    b = remainder
print("最大公約数：", a)