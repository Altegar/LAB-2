from math import sin, cos, log10


def for_func(a, b, step):
    """
    Ця функція обчислює заданий вираз за допомогою циклу for
    :param a: початок діапазону табулювання
    :param b: кінець діапазону табулювання
    :param step: крок діапазону табулювання
    :return: повертається список з отриманими значеннями
    :rtype: list
    """
    lst = []
    for x in range(a, b + 1, step):
        y = 2 * (x ** 2 - 3) - (sin(x ** 2) / 1 + cos(x)) + (cos(abs(x)) ** 2) - log10(abs(x) + 2) - 1 + sin(x) ** 2
        lst.append(round(y, 3))
    return lst


def while_func(a, b, step):
    """
    Ця функція обчислює заданий вираз за допомогою циклу while
    :param a: початок діапазону табулювання
    :param b: кінець діапазону табулювання
    :param step: крок діапазону табулювання
    :return: повертається список з отриманими значеннями
    :rtype: list
    """
    lst = []
    x = a
    while x <= b:
        y = 2 * (x ** 2 - 3) - (sin(x ** 2) / 1 + cos(x)) + (cos(abs(x)) ** 2) - log10(abs(x) + 2) - 1 + sin(x) ** 2
        lst.append(round(y, 3))
        x += step
    return lst


def slice_func(a, b, step, lst):
    """
    Ця функція виконує операцію зрізання заданого списку
    :param a: початок зрізу
    :param b: кінець зрізу
    :param step: крок зрізу
    :param lst: список
    :return: повертається список з отриманими значеннями
    :rtype: list
    """
    return lst[a:b:step]


def sum_func(lst):
    """
    Ця функція обчислює суму всіх елементів заданого списку
    :param lst: список
    :return: повертається сума округлена до 3 чисел після крапки
    :rtype: int
    :rtype: float
    """
    sum_value = 0
    for i in lst:
        sum_value += i
    return round(sum_value, 3)


def max_func(lst):
    """
    Ця функція знаходить максимальний елемент у заданому списку
    :param lst: список
    :return: повертається максимальний елемент
    :rtype: int
    :rtype: float
    """
    max_value = lst[0]
    for i in lst:
        if i > max_value:
            max_value = i
    return max_value


def min_func(lst):
    """
    Ця функція знаходить мінімальний елемент у заданому списку
    :param lst: список
    :return: повертається мінімальний елемент
    :rtype: int
    :rtype: float
    """
    min_value = lst[0]
    for i in lst:
        if i < min_value:
            min_value = i
    return min_value


if __name__ == "__main__":
    print("This is my module")
