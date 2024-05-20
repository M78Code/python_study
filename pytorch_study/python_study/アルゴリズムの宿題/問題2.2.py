# 問題2.2（教科書の問題 2.1-4 p.25）
# サイズnの配列A[1:n]にデータが格納されている。値aに等しいデータA[i]があれば
# そのインデックスいを出力し、なければ0を出力する。順次探索法のプログラムを作れ。
def order_find(arr: list, a) -> int:
    """
    arr: 配列A[1:n]
    a:   値a
    len(arr): サイズn
    """
    if len(arr) == 0:
        return -1
    for i in range(len(arr)):
        if a == arr[i]:
            return i
    else:
        return 0


def _test_result():
    data_arr = [1, 4, 7, 2, 3, 5, 8, 9, 10, 11, 6, 15, 12]

    result = order_find(data_arr, 17)  # 値a = 7のとき
    print(result)  # インデックス2を出力した
    result = order_find(data_arr, 12)  # 値a = 9のとき
    print(result)  # インデックス7を出力した
    result = order_find(data_arr, 117)  # 値a = 17のとき
    print(result)  # インデックス0を出力した


_test_result()
