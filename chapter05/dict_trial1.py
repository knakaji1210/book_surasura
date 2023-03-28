# coding:utf-8
fruits_dict = {'apple':100, 'orange':150}
if 'apple' in fruits_dict:
    print('appleはfruitsの中にあります')
if 'tomato' not in fruits_dict:
    print('tomatoはfruitsの中にありません')
if 100 not in fruits_dict:
    print('100はfruitsのkeyにはありません')
print(fruits_dict.values())
if 100 in fruits_dict.values():
    print('100はfruitsのvaluesにあります')