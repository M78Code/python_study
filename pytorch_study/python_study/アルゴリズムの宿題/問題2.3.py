# 問題2.3（教科書の問題 2.1-5 p.25）
import random


# サイズnの配列A[0:n-1]とB[0:n-1]
def _create_array(size: int) -> list:
    """
    create an array of size n.
    """
    # a と b の間の確率的な整数を生成する。
    array = []
    for i in range(0, size):
        random_number = random.randint(0, 1)
        array.append(random_number)
    return array


# eg: [1, 1, 0, 1, 0, 1, 0, 1, 1, 0]
def _binary_to_decimal(array: list) -> int:
    decimal_number = 0
    array_length = len(array)
    for i in range(array_length):
        decimal_number += array[i] * pow(2, array_length - i - 1)
    # s = ""
    # for e in array:
    #     s += str(e)
    # binary_number = int(s, 2)  # 2進数を表す
    # decimal_number = 0  # aとかbとか求め
    # weight_position = 0  # 桁
    #
    # while binary_number != 0:
    #     digit = binary_number & 1
    #     decimal_number += digit * pow(2, weight_position)
    #     binary_number >>= 1  # 右移一位，处理下一位
    #     weight_position += 1  # 桁加1

    return decimal_number


def generate_new_array() -> list:
    # サイズnの配列A[0:n-1]、例えばサイズは6である
    a_array = _create_array(6)
    # サイズnの配列B[0:n-1]、例えばサイズは6である
    b_array = _create_array(6)
    # 配列A[0:n-1]の2進数の合計を10進数に表現する
    sum_a = _binary_to_decimal(a_array)
    # 配列B[0:n-1]の2進数の合計を10進数に表現する
    sum_b = _binary_to_decimal(b_array)
    # 配列C[0:n]のサイズはcである
    c = sum_a + sum_b
    # 生成した配列C
    c_array = _create_array(c)
    return c_array


test_data = [1, 1, 0, 1, 0, 1, 0, 1, 1, 0]
ka = _binary_to_decimal(test_data)
print("ka = ", ka)


# test_decimal = _binary_to_decimal(test_data)
# test1 = int("1101010110", 2)
# print("test1 = ", test1)
# print(test_decimal)


def _list_to_string(array: list) -> str:
    s = ""
    for e in array:
        s += str(e)
    return s

# result1 = _list_to_string(result)
# print(result1)
# print(type(result))
# result2 = int(result1, 10)
# print(result2)
# print(type(result2))


