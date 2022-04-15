# Задача 2
# Заданы размеры коробки box_x, box_y и товара product_x, product_y
# Определить, поместится ли товар в коробке (габариты товара параллельны размеру коробки)
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные
# проверить для
# product_x, product_y = 9, 8
# product_x, product_y = 8, 6
# product_x, product_y = 3, 4
# product_x, product_y = 11, 9
# product_x, product_y = 9, 11

# Раскомментируйте нужную строку

box_x, box_y = 10, 7
product_x, product_y = 8, 9
if product_x <= box_x and product_y <= box_y:
    print('ДА')
else:
    print('НЕТ')
