
# https://leetcode.com/problems/contains-duplicate/


"""
1. Create set

2. Iterate over list/string, check if value already present in set
    If so: return true

3. If no duplicates found, return false outside loop


"""


def contains_duplicate_sort(nums):
    # Time: O(nlogn)
    # Space: O(1)
    nums.sort()

    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]:
            return True
    return False


def contains_duplicate(nums):
    # Time O(N)
    # Space O(N)

    unique = set()

    for num in nums:
        if num in unique:
            return True
        else:
            unique.add(num)
    return False


if __name__ == '__main__':
    test1 = [1, 2, 3, 1]
    test2 = [1, 2, 3, 4]
    print(contains_duplicate(test1))
    print(contains_duplicate(test2))
    print(contains_duplicate_sort(test1))
    print(contains_duplicate_sort(test2))
