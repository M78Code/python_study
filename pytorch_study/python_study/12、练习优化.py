# 求100以内所有的质数
# count = 0
# i = 2
# while i <= 100000:
#     flag = True
#     j = 2
#     while j<i:
#         if i % j == 0:
#             flag = False
#             # 未加break时的优化exited with code=0 in 239.887 seconds
#         j += 1
#     if flag:
#         count += 1
#         # print(i)
#     i += 1
# else:
#     print(f"Prime count is {count}")


#  break # 第一次优化 exited with code=0 in 26.689 seconds
# count = 0
# i = 2
# while i <= 100000:
#     flag = True
#     j = 2
#     while j<i:
#         if i % j == 0:
#             flag = False
#             break
#         j += 1
#     if flag:
#         count += 1
#         # print(i)
#     i += 1
# else:
#     print(f"Prime count is {count}")

# 第二次优化 exited with code=0 in 0.227 seconds
count = 0
i = 2
while i <= 100000:
    flag = True
    j = 2
    while j <= i ** 0.5:
        if i % j == 0:
            flag = False
            break
        j += 1
    if flag:
        count += 1
        # print(i)
    i += 1
else:
    print(f"Prime count is {count}")
