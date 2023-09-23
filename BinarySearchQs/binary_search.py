

# https://leetcode.com/problems/binary-search/

# Given an array of integers nums which is sorted in ascending order,
# and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.


def binary_search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1


if __name__ == '__main__':
    nums1 = [-1, 0, 3, 5, 9, 12]
    target1 = 9

    nums2 = [-1, 0, 3, 5, 9, 12]
    target2 = 2

    nums3 = [1, 3, 6, 8, 9, 10]
    target3 = 6
    target4 = 5

    print(binary_search(nums1, target1))  # 4
    print(binary_search(nums2, target2))  # -1
    print(binary_search(nums3, target3))  # 2
    print(binary_search(nums3, target4))  # -1
