
"""
take a pos integer from user, display all twin prime
numbers equal or less than input number. 
twin prime numbers are prime numbers which have difference of two
If no twin prime, display 0. If input is non positive or 0, display -1

output, string of integers, twin preime separated by colon, each
pair separated by comma

input: 20, output: 3:5,5:7,11:13,17:19

3 -> 0

-8 -> -1


"""


# def twin_prime(num):
#     prime = [True for i in range(num + 2)]
#     p = 2

#     while (p * p <= num + 1):
#         if prime[p] == True:
#             for i in range(p * 2, num + 2, p):
#                 prime[i] = False
#         p += 1

#     for p in range(2, num-1):
#         if prime[p] and prime[p + 2]:
#             print(p, ":", (p + 2), ",", end='')


# twin_prime(20)

from math import sqrt


def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    for i in range(5, int(sqrt(num)+1), 6):
        if (num % i == 0) or (num % i + 1 == 0):
            return False

    return True


def find_twin_primes(num):

    if num <= 0:
        return -1

    ret = ''

    for i in range(2, num + 2):
        if is_prime(i-2) and is_prime(i):
            ret += str(i-2) + ':' + str(i) + ','

    # if ret:
    #     return ret[:-2]
    # else:
    #     return 0

    return ret[:-1] if ret else 0


if __name__ == '__main__':
    print(find_twin_primes(20))  # 3:5, 5:7, 11:13, 17:19
    print(find_twin_primes(3))  # 0
    print(find_twin_primes(-8))  # -1
