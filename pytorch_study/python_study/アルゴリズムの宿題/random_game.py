import random


def _input_keyboard_text():
    change_role = True
    random_number = random.randint(0, 9)
    print(f'適任する候補者{random_number}')
    while change_role:
        if change_role:
            user_input = input('(0~9)入力してください: ')
            if user_input.isdigit():
                str_to_int = int(user_input)
                if str_to_int == random_number:
                    print(f'現在の秘書👩‍💼候補者を解雇し、候補者{str_to_int}を雇用する')
                    print('-------------------------------')
                    print('他の候補者も見てみたいですか？')
                    print('yを入力してから、続き；nを入力してから、終わりです。')
                    continue_ = input('(y or n)を入力してください: ')
                    if continue_ == 'y':
                        change_role = True
                        random_number = random.randint(0, 9)
                        print(f'新しく適任する候補者{random_number}')
                    else:
                        change_role = False
                else:
                    print(f'候補者{str_to_int}は適任できません。')
            else:
                print('入力エラー、0~9の数字です。')
    else:
        print('Congratulations on your successful application! 頑張ってね')


# _input_keyboard_text()

def _coin_test():
    a = []
    n = 10
    for index in range(0, n):
        ran_num = random.randint(0, 1)
        a.append(ran_num)
    return a


if __name__ == '__main__':
    result = _coin_test()
    arr_0 = []
    arr_1 = []
    for i in result:
        if i == 0:
            arr_0.append(i)
        else:
            arr_1.append(i)

    print(arr_0)
    print(arr_1)
    print(f"投げると表が確率a={len(arr_0)}/{len(result)}, 裏が確率1-a={len(arr_1)}/{len(result)}")
