x = 10000
for i in range(x):
    for j in range(x):
        k = j * i
    # print('进度',f'|{"#" * ((i+1)*50//x):50}|',
    #       f'{(i+1)*100//x}%',
    #       end='\r')
    # print(i) 白金选手
    print(f'{i+1} / {x}', end='\r')
print('\n完成！ ')

