# coding:utf-8

num = 10

def make_num():
    num = 20
    print('ローカル変数は', num)

make_num()

print('ローカル変数外は', num)