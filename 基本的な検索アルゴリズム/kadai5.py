import numpy as np  # マスの座標をnumpyを使って行列に格納する
import sys  # プログラムを共生的に終了する時に使う(エラーが出た時など)
import queue  # 幅優先と深さ優先の処理ではキューとスタックのクラスを使用する
sys.setrecursionlimit(10000)

message = ["幅優先検索", "深さ優先探索"]
matrix = np.zeros((101, 101))
file_number = 0


def next(genzaichi, CL):
    
    # クローズリスト（CL）と現在地の座標（現状態：genzaichi=[x,y]）を引数としている。
    # また、次の進めるマスの座標（リスト型）のリストを返却値としている。
    
    move_list = []  # リストの定義
    x = genzaichi[0]  # x 座標
    y = genzaichi[1]  # y 座標

    for i in (x - 1, x + 1):  # 現在位置の上のマスと下のマスを調べる
        # クローズリストに存在しなければmove_listに入れる
        if matrix[i,y] == 0 and ([i,y] not in CL):
            move_list.append([i, y])
    for j in (y - 1, y + 1):  # 現在位置の右と左のマスを調べる
        # クローズリストに存在しなければmove_listに入れる
        if matrix[x, j] == 0 and ([x, j] not in CL):
            move_list.append([x, j])
    return move_list  # 次に進めるマスのリストを返却する


def search(OL, CL):
    # STEP-2: OL={}ならばfalseを返して終了
    if OL.empty():
        print("Error: Openlist is empty.")
        sys.exit()  # プログラム終了

    # STEP-3: xをOLから取り出す
    else:
        genzaichi = OL.get()

        # STEP-4: xがゴール状態ならば True を返して終了
        if genzaichi[0] == 99 and genzaichi[1] == 99:
            # print("map" + str(file_number) + "　において" + message[select_yusen] + "でゴールに到着した!!!")
            return

        # STEP-5: xをCLに追加
        else:
            CL.append(genzaichi)

        # STEP-6: OL に next(genzaichi, CL)の返却値を追加
        move_list = next(genzaichi, CL)
        next_count[select_yusen, file_number] += 1

        for i in move_list:
            OL.put(i)
        if OL.qsize() > olist_maxsize[select_yusen, file_number]:
            olist_maxsize[select_yusen, file_number] = OL.qsize()

        # STEP-7: Step 2 に戻る
        search(OL, CL)


def habayusen():
    # STEP-1: OL={1,1}, CL={}
    olist = queue.Queue(maxsize=10000)  # オープンリスト（これから探索するマスのリスト）をキューにして、幅優先で探索を行う
    olist.put([1, 1])  # 初期状態：現在地をオープンリストに追加
    clist = []  # 初期状態：探索はまだ行っていない
    global select_yusen
    select_yusen = 0
    search(olist, clist)  # 探索開始


def fukasayusen():
    # STEP-1: OL={1,1}, CL={}
    # 深さ優先ではオープンリストをスタックにする（LIFO=最後に入れたのが最初に出る）
    olist = queue.LifoQueue(maxsize=10000)
    olist.put([1, 1])  # 初期状態：現在地をオープンリストに追加
    clist = []  # 初期状態：探索はまだ行っていない
    global select_yusen
    select_yusen = 1
    search(olist, clist)  # 探索開始


def file_select():  # マップを選んで、そのマップにおいて検索を行う関数
    global file_number  # 現在のマップを記録する変数
    if file_number < 100:
        try:  # ファイル読み込みを行う
            f = open("map" + str(file_number))
            lines = f.readlines()
            for i in range(101):
                for j in range(101):
                    matrix[i, j] = lines[i][j]
        except IOError:  # エラーが出たらエラーメッセージを出力する
            print("ファイル読み込みにエラーが出た！")
            sys.exit()
        finally:
            f.close()
            habayusen()
            fukasayusen()
            file_number += 1  # マップのナンバーを記録する変数を1増やす
            file_select()  # 全てのマップ検索が終わるまで再帰
    else:
        return


def average(data, temp=0):  # 平均値
    for i in range(100):
        temp += data[i]
    return temp / 100


def variance(data, temp=0):  # 分散地
    avrg = average(data)  #平均値を計算
    for i in range(100):
        temp += (data[i] - avrg) ** 2
    return temp / 100

select_yusen = 0
next_count = np.zeros((2, 100))
olist_maxsize = np.zeros((2, 100))
file_select()  # 迷路問題の検索を開始

print("\n計算量の平均値\n"
      "幅優先　：" + str(average(next_count[0])) + "\n" 
      "深さ優先：" + str(average(next_count[1])) + "\n")

print("計算量の分散値\n"
      "幅優先　：" + str(variance(next_count[0])) + "\n" 
      "深さ優先：" + str(variance(next_count[1])) + "\n")

print("計算量の最悪値\n"
      "幅優先　：" + str(max(next_count[0])) + "\n" 
      "深さ優先：" + str(max(next_count[1])) + "\n")

print("計算量の最良値\n"
      "幅優先　：" + str(min(next_count[0])) + "\n" 
      "深さ優先：" + str(min(next_count[1])) + "\n")

print("情報量の平均値\n"
      "幅優先　：" + str(average(olist_maxsize[0])) + "\n" 
      "深さ優先：" + str(average(olist_maxsize[1])) + "\n")

print("情報量の分散値\n"
      "幅優先　：" + str(variance(olist_maxsize[0])) + "\n" 
      "深さ優先：" + str(variance(olist_maxsize[1])) + "\n")

print("情報量の最悪値\n"
      "幅優先　：" + str(max(olist_maxsize[0])) + "\n" 
      "深さ優先：" + str(max(olist_maxsize[1])) + "\n")

print("情報量の最良値\n"
      "幅優先　：" + str(min(olist_maxsize[0])) + "\n" 
      "深さ優先：" + str(min(olist_maxsize[1])))
