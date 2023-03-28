# coding:utf-8
member = 4
today = '月'
if member >= 4:
    if today != '月':
        store = 'A'
    else:
        store = 'B'
else:
    store = 'C'
print('{}の店に行く'.format(store))