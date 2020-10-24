from functools import wraps


def trace(delimiter):
    def actual_wraps(func):
        lvl = 0

        @wraps(func)
        def wrapper(n):
            nonlocal lvl
            print(delimiter * (lvl), '-->', func.__name__ + '(' + str(n) + ')')
            lvl += 1
            val = func(n)
            lvl -= 1
            print(delimiter * (lvl), '<--', func.__name__ + '(' + str(n) + ')', '==', val)
            return val

        return wrapper

    return actual_wraps


@trace("____")
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


fib(5)

#Example work
#  --> fib(5)
# ____ --> fib(4)
# ________ --> fib(3)
# ____________ --> fib(2)
# ____________ <-- fib(2) == 1
# ____________ --> fib(1)
# ____________ <-- fib(1) == 1
# ________ <-- fib(3) == 2
# ________ --> fib(2)
# ________ <-- fib(2) == 1
# ____ <-- fib(4) == 3
# ____ --> fib(3)
# ________ --> fib(2)
# ________ <-- fib(2) == 1
# ________ --> fib(1)
# ________ <-- fib(1) == 1
# ____ <-- fib(3) == 2
#  <-- fib(5) == 5