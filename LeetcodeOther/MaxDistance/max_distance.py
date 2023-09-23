def find_max_distance(nums, target):
    indexes = []

    for i in range(len(nums)):
        if nums[i] == target:
            indexes.append(i)

    if len(indexes) < 2:
        return -1
    else:
        return (max(indexes) - min(indexes)) - 1


if __name__ == '__main__':
    x = [1, 3, 4, 5, 3, 7, 8, 9, 3]  # [1, 4, 8] -> 6
    print(find_max_distance(x, 3))

    j = [1, 3, 4, 5, 5, 7, 8, 9, 1]  # -> -1
    print(find_max_distance(j, 3))

    q = [1, 17, 4, 5, 5, 7, 8, 9, 1]  # - > 7
    print(find_max_distance(q, 1))

    f = [1, 1, 4, 5, 5, 7, 8, 9, 17]  # - > 0
    print(find_max_distance(f, 1))
