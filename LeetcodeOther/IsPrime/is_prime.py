
from math import sqrt


def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    for i in range(5, sqrt(num), 6):
        if (num % i == 0) or (num % i + 1 == 0):
            return False

    return True
