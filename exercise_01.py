# Задача 1
# Приведем список покупок в магазине
# Измените список согласно пунктам задания
# Выведите результат каждого пункта на консоль по очереди

#   а. Вставьте рыбу между горошком и рисом
#   b. Добавьте фрукты из списка fruits в конец списка shop_list
#   c. Удалите из списка shop_list картофель
#   d. Какими по счету стоят хлеб и апельсин? Выведите номера на консоль в формате
#   Номер "продукта" в списке - N 

#A
print('a.')
shop_list = ['Картофель', 'Горошек', 'Рис', 'Хлеб']
shop_list.insert(2, 'Рыба')
print(shop_list)
#B
print('b.')
fruits = ['Яблоко', 'Апельсин', 'Клубника']
shop_list += fruits
print(shop_list)
#C
print('c.')
shop_list.remove('Картофель')
print(shop_list)
#D
print('d.')
x = shop_list.index('Хлеб')
print('Номер Хлеба в списке -', x)
y = shop_list.index('Апельсин')
print('Номер Апельсина в списке -', y)