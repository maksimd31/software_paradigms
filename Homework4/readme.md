Коэффициент корреляции Пирсона является мерой линейной зависимости между двумя переменными. Он показывает, насколько сильно и в каком направлении связаны две переменные. Коэффициент корреляции Пирсона принимает значения от -1 до 1.

- Значение 1 означает положительную линейную зависимость, то есть при увеличении одной переменной, другая переменная также увеличивается пропорционально.
- Значение -1 означает отрицательную линейную зависимость, то есть при увеличении одной переменной, другая переменная уменьшается пропорционально.
- Значение 0 означает отсутствие линейной зависимости между переменными.

Коэффициент корреляции Пирсона может быть использован для определения степени и направления связи между различными переменными, такими как доход и расход, температура и продажи, или любые другие пары переменных, для которых имеются числовые данные.

```python
def correlation_pers(x, y):
    """
        Документирование функций по pep 257
        Вычисляет коэффициент корреляции Пирсона между двумя массивами x и y.

        Аргументы:
        x (list): Первый массив чисел.
        y (list): Второй массив чисел.

        Возвращает:
        float: Коэффициент корреляции Пирсона между массивами x и y.

        Примечания:
        Данная функция предназначена для вычисления коэффициента корреляции Пирсона
        и требует передачи двух массивов одинаковой длины в качестве аргументов.
        Коэффициент корреляции Пирсона принимает значения от -1 до 1.
    """
    average_x = sum(x) / len(x)
    average_y = sum(y) / len(y)
    # Получаем среднее значение x и y

    cov = sum((xi - average_x) * (yi - average_y) for xi, yi in zip(x, y))
    dev_x = (sum((xi - average_x) ** 2 for xi in x) / len(x)) ** 0.5
    dev_y = (sum((yi - average_y) ** 2 for yi in y) / len(y)) ** 0.5

    # вычисляем коэффициент корреляции Пирсона
    correlation = cov / (dev_x * dev_y)

    return correlation


# Проверка функции
if __name__ == '__main__':
    # Тестовые данные
    x = [1, 2, 3, 4, 5]
    y = [5, 4, 3, 2, 1]

    # Ожидаемый результат: -1.0 (отрицательная линейная зависимость)
    expected_result = -1.0

    # Вызов функции и получение результата
    result = correlation_pers(x, y)

    # Проверка результата
    if result == expected_result:
        print("Проверка пройдена: коэффициент корреляции соответствует ожидаемому результату.")
    else:
        print("Проверка не пройдена: коэффициент корреляции не соответствует ожидаемому результату.")


```
Функция `correlation_pers(x, y)` вычисляет коэффициент корреляции Пирсона между двумя массивами `x` и `y`.

1. Происходит вычисление средних значений `average_x` и `average_y` для массивов `x` и `y` соответственно.
2. Вычисляется ковариация `cov` и стандартное отклонение `dev_x` и `dev_y` для массивов `x` и `y`.
3. Коэффициент корреляции Пирсона `correlation` рассчитывается как отношение ковариации к произведению стандартных отклонений.
4. Функция возвращает значение коэффициента корреляции.

Примечание: Данная функция предназначена для вычисления коэффициента корреляции Пирсона и требует передачи двух массивов одинаковой длины в качестве аргументов.