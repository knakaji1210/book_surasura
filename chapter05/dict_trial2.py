fruits_dict = {'apple':100, 'orange':150, 'banana':200}
for fruit in fruits_dict:
    print(fruit)
for fruit_values in fruits_dict.values():
    print(fruit_values)
for key, value in fruits_dict.items():
    print(key, value)
for fruit_item in fruits_dict.items():
    key2 = fruit_item[0]
    value2 = fruit_item[1]
    print(key2,value2)