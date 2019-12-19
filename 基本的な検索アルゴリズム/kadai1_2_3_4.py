import numpy as np  # マスの座標をnumpyを使って行列に格納する
import sys  # プログラムを共生的に終了する時に使う(エラーが出た時など)
import queue  # 幅優先と深さ優先の処理ではキューとスタックのクラスを使用する

#######kadai1#######

try:  # ファイル読み込みを行う
    f = open("map1010.txt")
    lines = f.readlines()
    matrix = np.zeros((11, 11))
    for i in range(11):
        for j in range(11):
            matrix[i, j] = lines[i][j]

except IOError:  # エラーが出たのであればエラーメッセージを出力する
    print("ファイル読み込みにエラーが出た！")
    sys.exit()
finally:
    f.close()

print(matrix)

#######kadai2#######


def next(genzaichi, CL):
    """
    クローズリスト（CL）と現在地の座標（現状態：genzaichi=[x,y]）を引数としている。
    また、次の進めるマスの座標（リスト型）のリストを返却値としている。
    """
    move_list = []  # リストの定義
    x = genzaichi[0]  # x 座標
    y = genzaichi[1]  # y 座標

    for i in (x - 1, x + 1):  # 現在位置の上のマスと下のマスを調べる
        if matrix[i, y] == 0 and ([i, y] not in CL):  # クローズリストに存在しなければmove_listに入れる
            move_list.append([i, y])
    for j in (y - 1, y + 1):  # 現在位置の右と左のマスを調べる
        if matrix[x, j] == 0 and ([x, j] not in CL):  # クローズリストに存在しなければmove_listに入れる
            move_list.append([x, j])
    return move_list  # 次に進めるマスのリストを返却する


#######kadai3#######


def habayusen():
    # STEP-1: OL={1,1}, CL={}
    olist = queue.Queue()  # オープンリスト（これから探索するマスのリスト）をキューにして、幅優先で探索を行う
    olist.put([1, 1])  # 初期状態：現在地をオープンリストに追加
    clist = []  # 初期状態：探索はまだ行っていない
    search(olist, clist)  # 探索開始
    print("幅優先Close Listの中身:")
    print(clist)


def search(OL, CL):
    # STEP-2: OL={}ならばfalseを返して終了
    if OL.empty():
        print("Error: Openlist is empty.\n")
        sys.exit()  # プログラム終了

    # STEP-3: xをOLから取り出す
    else:
        genzaichi = OL.get()

        # STEP-4: xがゴール状態ならば True を返して終了
        if genzaichi[0] == 9 and genzaichi[1] == 9:
            print("ゴールに到着した")
            return
        # sys.exit()

        # STEP-5: xをCLに追加
        else:
            CL.append(genzaichi)

        # STEP-6: OL に next(genzaichi, CL)の返却値を追加
        move_list = next(genzaichi, CL)
        for i in move_list:
            OL.put(i)

        # STEP-7: Step 2 に戻る
        search(OL, CL)

############ KADAI4 #############


def fukasayusen():
    #  STEP-1: OL={1,1}, CL={}
    olist = queue.LifoQueue()  # 深さ優先ではオープンリストをスタックにする（LIFO=最後に入れたのが最初に出る）
    olist.put([1, 1])  # 初期状態：現在地をオープンリストに追加
    clist = []  # 初期状態：探索はまだ行っていない
    search(olist, clist)  # 探索開始
    print("深さ優先Close Listの中身:")
    print(clist)

habayusen()
fukasayusen()
