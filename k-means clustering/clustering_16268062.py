
import matplotlib.pyplot as plt
import numpy as np
X = np.loadtxt("./iris4d.txt")
(d, n) = X.shape  # 行数と列数を取得
# STEP-1
print("N:")
N = int(input())


def dis(x, y, cov):  # Mahalanobis 距離の計算
    dist = np.dot(np.dot((x-y).T, cov), (x-y))
    return dist


# STEP-2
c = np.zeros((d, N))
for i in range(N):
    c[:, i] = X[:, N-1-i]  #データの最初のN個の要素
print("セントロイドの初期値：")
print(c)
control = np.zeros((d, N))

flag = 1
cov = np.cov(X)
while flag:  # print("girdi")
    for i in range(d):
        for j in range(N):
            control[i,j] = c[i, j]  # 前のセントロイドを保存する
    S = []
    for i in range(N):
        S.append([])  # N個の行列を要素とするリスト
    d_mhlnbs = [0]*N

    for i in range(n):
        for j in range(N):
            d_mhlnbs[j] = dis(X[:, i], c[:, j], cov)  #マハラノビス距離
        min_d = d_mhlnbs.index(min(d_mhlnbs))    # 一番近い代表のクラスを取得
        S[min_d].append(X[:, i])  # 一番近い代表のクラスに入れる

    # グラフの用意
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    color_list = ["r", "g", "b", "c", "m", "y", "k", "w"]
    for i in range(N):
        for j in range(len(S[i])):
            ax.scatter(S[i][j][0], S[i][j][1], c=color_list[i % len(color_list)], marker='.', label='group1')
    fig.show()

    # セントロイドを更新
    for i in range(N):
        for j in range((len(S[i]))):
            summ = 0
            for k in range((len(S[i]))):
                summ = summ + dis(S[i][j], S[i][k], cov)
            if j == 0:
                min_value = summ
                min_index = j
            elif summ < min_value:
                min_value = summ
                min_index = j
        c[:, i] = S[i][min_index]
    print("新しいセントロイド：")
    print(c)
    flag = 0
    # 前のセントロイドと更新したものが同じであれば終了
    for i in range(d):
        for j in range(N):
           if c[i, j] != control[i, j]:
                flag = 1
