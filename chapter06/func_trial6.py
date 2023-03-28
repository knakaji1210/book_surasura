def make_greet(name):
    greet = 'Hello {}-san'.format(name)
    return greet

for name in ['Sato', 'Suzuki', 'Tanaka']:
    print(make_greet(name))

print('last one')
print(make_greet('Hasegawa'))