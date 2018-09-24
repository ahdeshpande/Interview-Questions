# Write methods to implement the multiply, subtract, and divide operations for
#  integers. Use only the add operator:


def negate(num):
    neg = 0

    d = 1 if num < 0 else -1
    while num != 0:
        neg += d
        num += d

    return neg


def absolute(num):
    return negate(num) if num < 0 else num


def subtract(a, b):
    return a + negate(b)


def multiply(a, b):
    if a < b:
        return multiply(b, a)

    total = 0

    for i in range(absolute(b), 0, -1):
        total += a

    return negate(total) if b < 0 else total


def divide(a, b):
    if b == 0:
        return ZeroDivisionError

    absolute_a = absolute(a)
    absolute_b = absolute(b)

    product = 0
    x = 0

    while product + absolute_b <= absolute_a:
        product += absolute_b
        x += 1

    return x if a < 0 and b < 0 or a > 0 and b > 0 else negate(x)


print(divide(42, 0))
