num = 10

def make_num(num):
    local_num = num + 10
    print('ローカル変数は', local_num)

make_num(num)

print('ローカル変数外は', num)