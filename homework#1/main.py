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


print('Squaring: ', exponentiation(1, 2, 3))
print('Exponentiation:', exponentiation(1, 2, 3, power=3))

#Example work
# Squaring:  [1, 4, 9]
# Exponentiation: [1, 8, 27]


def is_prime(num):
    """
    Check is prim number or not
    :param num:
    :return bool:
    """
    result = []
    for i in range(1, num+1):
        if num % i == 0:
            result.append(i)
    if set(result) == set([1, num]):
        return True
    return False


#Написать функцию, которая на вход принимает список из целых чисел, и возвращает только чётные/нечётные/простые числа
# (выбор производится передачей дополнительного аргумента)
def filter_numbers(*args, type_filter=None):
    """
    Checks numbers for even/odd/prime
    :param args:
    :param type_filter:
    :return:
    """
    if type_filter == 'EVEN_NUMBERS':
        return list(filter(lambda x: x % 2 == 0, args))
    elif type_filter == 'ODD_NUMBERS':
        return list(filter(lambda x: x % 2 != 0, args))
    elif type_filter == 'PRIME_NUMBERS':
        return list(filter(is_prime, args))
    else:
        print('Filter not specified or not defined')
        sys.exit(1)


print('Only even:', filter_numbers(1, 3, 4, 5, 8, 9, type_filter='EVEN_NUMBERS'))
print('Only odd:', filter_numbers(1, 3, 4, 5, 8, 9, type_filter='ODD_NUMBERS'))
print('Prime number:', filter_numbers(1, 3, 4, 5, 8, 9, type_filter='PRIME_NUMBERS'))

#Example work
# Only even: [4, 8]
# Only odd: [1, 3, 5, 9]
# Prime number: [1, 3, 5]


#Создать декоратор для замера времени выполнения функции
def benchmark(func):
    @wraps(func)
    def wrapper(*args):
        time_start = time.time()
        func(*args)
        time_end = time.time()
        print('Time run: ', time_end-time_start)
    return wrapper


@benchmark
def example():
    print('Start function')
    time.sleep(2)
    print('End function')


example()

#Example work
# Start function
# End function
# Time run:  2.0008256435394287