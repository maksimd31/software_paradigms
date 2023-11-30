# Homework6 
### Бинарный поиск
● Контекст

Предположим, что мы хотим найти элемент в массиве (получить
его индекс). Мы можем это сделать просто перебрав все элементы.
Но что, если массив уже отсортирован? В этом случае можно
использовать бинарный поиск. Принцип прост: сначала берём
элемент находящийся посередине и сравниваем с тем, который мы
хотим найти. Если центральный элемент больше нашего,
рассматриваем массив слева от центрального, а если больше -
справа и повторяем так до тех пор, пока не найдем наш элемент.

● Ваша задача

Написать программу на любом языке в любой парадигме для
бинарного поиска. На вход подаётся целочисленный массив и
число. На выходе - индекс элемента или -1, в случае если искомого
элемента нет в массиве.

### Решение

```python
# Рекурсивный бинарный поиск
def binary_search_recursive(arr, target):
    return binary_search_recursive_helper(arr, target, 0, len(arr) - 1)


def binary_search_recursive_helper(arr, target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive_helper(arr, target, left, mid - 1)
    else:
        return binary_search_recursive_helper(arr, target, mid + 1, right)


# Итеративный бинарный поиск
def binary_search_iterative(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1


if __name__ == '__main__':
    # Демонстрация использования
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 5

    index_recursive = binary_search_recursive(arr, target)
    index_iterative = binary_search_iterative(arr, target)

    print("Рекурсивный бинарный поиск:")
    if index_recursive != -1:
        print("Индекс элемента", target, ":", index_recursive)
    else:
        print("Элемент", target, "не найден")

    print("\\nИтеративный бинарный поиск:")
    if index_iterative != -1:
        print("Индекс элемента", target, ":", index_iterative)
    else:
        print("Элемент", target, "не найден")

```