

def min_operations(num):
    # allowed operations:
    #   multiply by 2
    #   add 1

    count = 0
    while num != 0:
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1
        count += 1

    return count


if __name__ == '__main__':
    print(min_operations(6))
    print(min_operations(8))
    print(min_operations(7))
