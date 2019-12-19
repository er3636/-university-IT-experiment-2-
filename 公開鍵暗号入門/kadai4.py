from math import sqrt
import matplotlib.pyplot as plt
import timeit
import numpy as np

variable = 100

#print("数：")
#number = int(input())

# 素数判定
def prime_number(number):
    flag = 0  # numberが素数である場合は flag=0 のままである
    if number == 0 or number == 1:  # numberは0か1の時は調べない
        print(number, "は素数ではない")
        return

    # 2からルート(number)までが割り切れるかどうか調べる
    for j in range(2, int(np.sqrt(number))+1):
        # 割り切れれば flag=1 (素数ではない)
        if number % j == 0:
            flag = 1
            break

    if flag != 1:
        print(number, "は素数である")
    else:
        print(number, "は素数ではない")

elapsed_time = [0]
bits_time = [0]*len(bin(variable)[2:])
counter = [0]*len(bin(variable)[2:])

for i in range(1, variable):
    a = timeit.timeit("prime_number(i)", globals=globals(), number=1)
    elapsed_time.append(a)
    bits_time[len(bin(i)[2:])-1] += elapsed_time[i-1]
    counter[len(bin(i)[2:])-1] += 1
for i in range(len(bits_time)):
    bits_time[i] = bits_time[i] / counter[i]


plt.plot(list(range(len(bits_time))), bits_time)
plt.show()
#plt.plot(counter[i],bits_time[i])
#plt.show()