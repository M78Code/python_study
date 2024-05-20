# 問題2.2（教科書の問題 2.1-4 p.25）
# サイズnの配列A[1:n]にデータが格納されている。値aに等しいデータA[i]があれば
# そのインデックスいを出力し、なければ0を出力する。順次探索法のプログラムを作れ。

# 実験の配列のデータ
test_array = [3, 5, 1, 2, 10, 13, 6, 4]


def order_query(a):
    for i in range(len(test_array)):
        if a == test_array[i]:
            print(f"値a={a}は配列A[1:n]にあります、インデックスは{i}です。")
        else:
            print(f"値a={a}は配列A[1:n]にありません、0を出力しました。")


# a = 7のとき
# a = 1の時
# a = 13の時
order_query(7)
order_query(1)
order_query(13)

# 問題2.3（教科書の問題 2.1-5 p.25）
# サイズnの配列A[0:n-1]とB[0:n-1]
test_a_array = [0, 1, 1, 0, 1, 0, 1, 0]
test_b_array = [1, 1, 0, 1, 0, 0, 1, 1]


def create_new_array():
    sum_a = 0
    # サイズnの配列A[0:n-1]、例えばサイズは8である
    test_a_array_len = len(test_a_array)
    for i in range(test_a_array_len):
        # 配列A[0:n-1]の2進数の合計を10進数に表現する
        sum_a = sum_a + 2 ** (test_a_array_len - 1 - i)

    sum_b = 0
    # サイズnの配列B[0:n - 1]、例えばサイズは8である
    test_b_array_len = len(test_b_array)
    for i in range(test_b_array_len):
        # 配列B[0:n-1]の2進数の合計を10進数に表現する
        sum_b = sum_b + 2 ** (test_b_array_len - 1 - i)

    # 配列C[0:n]のサイズはcである
    c = sum_a + sum_b
    print("c = ", c)  # c = 510
    # 生成した配列C
    test_c_array = [0] * c
    print(f"生成した配列Cは{test_c_array}です。")


create_new_array()
