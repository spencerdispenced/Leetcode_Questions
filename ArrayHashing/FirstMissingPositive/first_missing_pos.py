def smallest_missing_int(nums):
    # Time: O(n)

    pos_ints = {}

    # map pos ints in list to dictionary
    for i in range(len(nums)):
        if nums[i] > 0:
            if nums[i] not in pos_ints.keys():
                # create key pair if not present
                pos_ints[nums[i]] = 0

            # increment value by 1 if found
            pos_ints[nums[i]] += 1

    print(pos_ints)

    # start at min possible missing positive, '1'
    # check if number is missing from keys in map
    # return if missing, else increment
    missing_positive = 1
    while (1):
        if missing_positive not in pos_ints.keys():
            return missing_positive

        missing_positive += 1


if __name__ == '__main__':
    arr = [-5, 2, 0, -1, -10, 15]
    arr2 = [3, 9, 5, 1, 7, 6, 8, 2]
    arr3 = [1, 2, 0]
    print(smallest_missing_int(arr3))  # 1
