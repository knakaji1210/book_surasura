numbers = [1, 2, 3, 4, 5, 6]
odd_list = []
even_list = []
for number in numbers:
    if number % 2 == 1:
        odd_list.append(number)
    elif number % 2 == 0:
        even_list.append(number)
print(odd_list)
print(even_list)