def multi(num):
    if not isinstance(num, int):
        print('Invalid num')
        return False
    multi_num = 100 * num
    print('multi_num is {}'.format(multi_num))
    return multi_num

def dev(num):
    if not isinstance(num, int):
        print('Invalid num')
        return False
    dev_num = num / 100
    print('dev_num is {}'.format(dev_num))
    return dev_num