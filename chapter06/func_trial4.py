def make_greet(name):
    greet = 'Hello {}-san'.format(name)
    return greet

greet_result = make_greet('Yamada')
print(greet_result)