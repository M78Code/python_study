# 問題2.8
# n個の実数データの中に和がちょうどxになるような２つの数が存在するかどうかを判定する計算量Θ(nIn(n))のプログラムを作れ。

# 编写一个时间复杂度为θ(nIn(n)) 的程序，判断 n 个实数数据中是否有两个数的和恰好为 x。

array = [13, 1, 27, 10, 8, 20, 33, 5, 7, 11, 12]


def merge_sort(arr: list):
    """マージソート"""
    if len(arr) == 1:
        print(f"再帰の終わり条件{arr}")
        return arr
    # 二分法を使用して配列arrを二つに分割する
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    # 再帰
    return __merge(merge_sort(left), merge_sort(right))


def __merge(left: list, right: list):
    print("===")
    result = []
    # 部分配列leftの長さをlen(left)
    # 部分配列rightの長さをlen(right)
    while len(left) > 0 and len(right) > 0:
        # 左の数が右の数より小さい場合、左の数は前に格納される
        if left[0] <= right[0]:
            result.append(left.pop(0))
        # 右の数が左の数より小さい場合、右の数は前に格納される
        else:
            result.append(right.pop(0))
    # 値は一つの配列にしかない場合、直接追加する
    result += left
    result += right
    return result


# test_result = merge_sort(array)
# print("最後のソートした結果:", test_result)


def has_two_sum(nums: list, x: int) -> bool:
    """
    配列numsの中に和がちょうどxになるような２つの数が存在するかどうかを判定する
    """
    # 对数组进行排序，利用归并排序算法，时间复杂度为Θ(nIn(n))
    sort_result = merge_sort(nums)
    left = 0
    right = len(sort_result) - 1
    while left < right:
        target_sum = sort_result[left] + sort_result[right]
        if target_sum == x:
            return True
        elif target_sum < x:
            left += 1
        else:
            right -= 1
    return False


# print(has_two_sum(array, 5))


def calcu_det():
    a = [[1, 3], [7, 5]]
    b = [[6, 8], [4, 2]]


list2d = [[1, 3], [7, 5, 6]]
for i in range(len(list2d)):
    for j in range(len(list2d[i])):
        print(list2d[i][j])
