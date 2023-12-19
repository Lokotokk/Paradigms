# Контекст
# Предположим, что мы хотим найти элемент в массиве (получитьего индекс). Мы можем это сделать просто перебрав все элементы.
# Но что, если массив уже отсортирован? В этом случае можно использовать бинарный поиск. 
# Принцип прост: сначала берём элемент находящийся посередине и сравниваем с тем, который мы хотим найти. 
# Если центральный элемент больше нашего, рассматриваем массив слева от центрального, а если больше - справа 
# и повторяем так до тех пор, пока не найдем наш элемент.
# ● Ваша задача
# Написать программу на любом языке в любой парадигме для бинарного поиска. На вход подаётся целочисленный массив и число. 
# На выходе - индекс элемента или -1, в случае если искомого элемента нет в массиве.

my_list = [0, 1, 2, 4, 6, 7, 11, 12, 25, 32]
element = 12
some_list_sort = sorted(my_list)
print(some_list_sort)

def find_el(some_list: list, start_index, find_element) -> int:

    right_index = len(some_list) - 1

    while start_index < right_index:
        center = start_index + (right_index - start_index) // 2
        if some_list[center] == find_element:        
            return center

        if some_list[center] > find_element:
            right_index = center - 1
        else:
            start_index = center + 1

    return -1  
 
print(find_el(some_list_sort, 0, element))