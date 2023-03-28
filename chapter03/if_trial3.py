# coding:utf-8
member = 3
if member == 1:
    store = 'A'
elif member == 2:
    store = 'B'
elif member <= 4:
    store = 'C'
else:
    store = 'D'
print('{}の店に行く'.format(store))