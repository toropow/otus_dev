from operator import pow
import sys
from functools import wraps
import time


# Написать функцию, которая принимает N целых чисел и возвращает список квадратов эих чисел.
# Бонусом будет сделать keyword аргумент для выбора степени, в которую будут возводиться числа
def exponentiation(*args, power=2):
    """
    Raises a set of numbers to a power
    :param args: Number for power
    :param power: Power
    :return list: Number to power
    """
    return list(map(lambda x: pow(x, power), args))


def is_prime(num):
    """
    Check is prim number or not
    :param num:
    :return bool:
    """
    if num == 1:
        return True
    elif num < 1:
        raise Exception('Only positive value')
    i = 2
    while num % i != 0:
        i += 1
    return i == num


EVEN_NUMBERS = 'even'
ODD_NUMBERS = 'odd'
PRIME_NUMBERS = 'prime'


# Написать функцию, которая на вход принимает список из целых чисел, и возвращает только чётные/нечётные/простые числа
# (выбор производится передачей дополнительного аргумента)
def filter_numbers(*args, type_filter=None):
    """
    Checks numbers for even/odd/prime
    :param args:
    :param type_filter:
    :return:
    """
    if type_filter == 'even':
        return list(filter(lambda x: x % 2 == 0, args))
    elif type_filter == 'odd':
        return list(filter(lambda x: x % 2 != 0, args))
    elif type_filter == 'prime':
        return list(filter(is_prime, args))
    else:
        print('Filter not specified or not defined')
        sys.exit(1)


# Создать декоратор для замера времени выполнения функции
def benchmark(func):
    @wraps(func)
    def wrapper(*args):
        time_start = time.time()
        func(*args)
        time_end = time.time()
        print('Time run: ', time_end - time_start)

    return wrapper


@benchmark
def example():
    print('Start function')
    time.sleep(2)
    print('End function')


if __name__ == '__main__':
    # Возведение в степень
    print('Squaring: ', exponentiation(1, 2, 3))
    print('Exponentiation:', exponentiation(1, 2, 3, power=3))

    # Example work
    # Squaring:  [1, 4, 9]
    # Exponentiation: [1, 8, 27]

    # Сортировка
    print('Only even:', filter_numbers(1, 3, 4, 5, 8, 9, type_filter=EVEN_NUMBERS))
    print('Only odd:', filter_numbers(1, 3, 4, 5, 8, 9, type_filter=ODD_NUMBERS))
    print('Prime number:', filter_numbers(1, 3, 4, 5, 8, 9, type_filter=PRIME_NUMBERS))

    # Example work
    # Only even: [4, 8]
    # Only odd: [1, 3, 5, 9]
    # Prime number: [1, 3, 5]

    # Замер времени
    example()

    # Example work
    # Start function
    # End function
    # Time run:  2.0008256435394287
