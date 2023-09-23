

def ceil_and_floor(nums,  target):
    low = 0
    high = len(nums) - 1

    if (target == 0):
        return -1

    while (low <= high):
        mid = low + (high - low) / 2
        mid = int(mid)
        if (nums[mid] == target):
            return mid
        elif (target < nums[mid]):
            high = mid - 1
        else:
            low = mid + 1

    return [nums[low], nums[high]]


def print_ceil_floor(cf, target):
    if (cf == -1):
        print("Ceiling and floor of", target, "does not exist in an array")
    else:
        print("Ceiling and floor of", target, "is", cf)


# [1, 4, 6, 8, 9] target = 3 -> [4, 1]
if __name__ == '__main__':
    nums1 = [1, 4, 6, 8, 9]
    target1 = 3

    nums2 = [1, 4, 6, 8, 9]
    target2 = 7

    print_ceil_floor(ceil_and_floor(nums1, target1),  target1)
    print_ceil_floor(ceil_and_floor(nums2, target2),  target2)
