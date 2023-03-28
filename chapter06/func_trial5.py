def make_greet(name):
    greet = 'Hello {}-san!'.format(name)
    return greet

print(make_greet('Sato'))
print(make_greet('Suzuki'))
print(make_greet('Tanaka'))
print('last one')
print(make_greet('Hasegawa'))