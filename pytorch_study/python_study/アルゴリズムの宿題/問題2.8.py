# 問題2.8
# n個の実数データの中に和がちょうどxになるような２つの数が存在するかどうかを判定する計算量Θ(nIn(n))のプログラムを作れ。

# 编写一个时间复杂度为θ(nIn(n)) 的程序，判断 n 个实数数据中是否有两个数的和恰好为 x。
test_arr = [13, 1, 27, 10, 8, 20, 33, 5, 7, 11, 12]


def merge(arr: list, left: int, right: int, mid: int, temp: list):
    """
    @param arr      元の配列
    @param left     左の配列の最初インデックス
    @param right    右のインデックス
    @param mid      中インデックス
    @param temp     仮の配列
    """
    i = left  # init the index of the left ordered sequence
    j = mid + 1  # init the index of the right ordered sequence
    t = 0  # init the index of the temp_arr

    # first step
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[t] = arr[i]
            i += 1
            t += 1
        else:
            temp[t] = arr[j]
            j += 1
            t += 1
    while i <= mid:  # 左の部分配列をtemp_arr配列にコピーする
        temp[t] = arr[i]
        t += 1
        i += 1
    while j <= right:  # 右の配列をtemp_arr配列にコピーする
        temp[t] = arr[j]
        t += 1
        j += 1
    t = 0
    # temp_arr配列の中で全要素を元配列arrにコピーする
    while left <= right:
        arr[left] = temp[t]
        left += 1
        t += 1

    print(f"arr = {arr}")


def merge_sort(arr: list, left: int, right: int, temp: list):
    if left < right:
        mid = (left + right) // 2
        # 左から
        merge_sort(arr, left, mid, temp)
        # 右から
        merge_sort(arr, mid + 1, right, temp)
        # マージ
        merge(arr, left, mid, right, temp)


def __test_main__():
    arr = [8, 4, 5, 7, 1, 3, 6, 2]
    temp_arr = [None] * len(arr)
    merge_sort(arr, 0, len(arr) - 1, temp_arr)
    print(f"マージソートの後で、結果は：{arr}")


__test_main__()


# for ide in range(1, 4):
#     print(f"ide = {ide}")


def merge__(arr: list, p: int, q: int, r: int, temp1_arr: list, temp2_arr: list):
    """
    arrは配列A[p:q]である
    pはpである
    qはqである
    rはrである
    temp1_arrは配列L[1:nL]である
    temp2_arrは配列R[1:nR]である
    例えば：p = 0,q = 3,r = 7
    A = [8,4,5,7,1,3,6,2]となる
    配列A[p:q] = [8,4,5,7]の長さnL = q-p+1 = 3-0+1 = 4
    配列A[q+1:r]=[1,3,6,2]の長さnR = r-q = 7-3 = 4
    """

    # 部分配列A[p:q]をL[1:nL]にコピーする
    for i in range(1, q - p + 1):
        temp1_arr[i] = arr[p + i]
    # 部分配列A[q+1:r]をR[1:nR]にコピーする
    for j in range(1, r - q):
        temp2_arr[j] = arr[q + j]
    i = 1
    j = 1
    k = p
    while i <= q - p + 1 and j <= r - q:
        if temp1_arr[i] <= temp2_arr[j]:
            arr[k] = temp1_arr[i]
            i += 1
        else:
            arr[k] = temp1_arr[j]
            j += 1
        k += 1
    while i <= q - p + 1:
        arr[k] = temp1_arr[i]
        i += 1
        k += 1
    while j <= r - q:
        arr[k] = temp1_arr[j]


def bubble_sort(arr: list) -> list:
    # 配列の長さを計算する
    arr_len = len(arr)
    """
    range関数の作用は順次数をなる
    外側のループは、最初から最後までのループ回数を制御する
    """
    for i in range(arr_len):  # outside loop
        # 数が交換されたかどうかを確認する
        is_change_num = False
        # 内側のループは1回歩くプロセスを制御する
        for j in range(arr_len - i - 1):  # inside loop
            # 前の数が次の数より大きい場合、２つの数を入れ替える（昇順）
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                # arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_change_num = True
        print(f"{i + 1}回目のソート後の配列は次の通りだ{arr}")
        if not is_change_num:
            return arr
    return arr


def _bubble_sort():
    result = bubble_sort(test_arr)
    print(result)


# _bubble_sort()


def __order(arr: list):
    for i in bubble_sort(arr):
        print(f"元素{i}")


# __order(test_arr)

# eg: arr = [1, 4, 13, 14, 17, 22, 35, 80, 91]
def _binary_search(arr: list, target: int) -> bool:
    """
    配列arrは昇順した配列A[1:n]
    targetは調べる値aである
    """

    # 配列arrのサイズn
    arr_len = len(arr)
    # 配列の左の最初のインデックス
    left_index = 0
    # 配列の右の最初のインデックス
    right_index = arr_len - 1

    while left_index <= right_index:
        # 配列の中のインデックス
        mid_index = (right_index - left_index) // 2
        if arr[mid_index] == target:
            return True
        elif arr[mid_index] < target:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return False
