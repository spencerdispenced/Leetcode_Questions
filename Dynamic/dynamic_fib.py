

def fib(n, memo={}):

    if n in memo:
        return memo[n]

    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
        return memo[n]


print(fib(0))
print(fib(2))
print(fib(6))
print(fib(9))
print(fib(100))
