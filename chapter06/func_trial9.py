# coding:utf-8

num = 10

def make_num():
    local_num = num + 10
    print('ローカル変数は', local_num)

make_num()

print('ローカル変数外は', num)