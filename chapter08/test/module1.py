def add(num):
    if not isinstance(num, int):
        print('Invalid num')
        return False
    add_num = 100 + num
    print('add_num is {}'.format(add_num))
    return add_num

def sub(num):
    if not isinstance(num, int):
        print('Invalid num')
        return False
    sub_num = 100 - num
    print('sub_num is {}'.format(sub_num))
    return sub_num
