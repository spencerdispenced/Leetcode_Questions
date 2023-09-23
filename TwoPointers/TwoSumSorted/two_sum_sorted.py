

# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.



Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].


1. Create left pointer set to index 0
   Create right pointer set to last index in input array

2. Loop while left pointer less than right pointer:

    2.1: Calculate current sum from respective pointer values

    2.2: If sum is greater than target:
            -Decrement right pointer

         If sum is less than target:
            -increment left pointer

         If sum matches target:
            -Return left and right indicies as array (+1 to each index for this problem, for some reason)

"""


def two_sum(nums, target):
    # Time: O(n), Space: O(1)
    left = 0
    right = len(nums) - 1

    while left < right:
        curr_sum = nums[left] + nums[right]

        if curr_sum > target:
            right -= 1
        elif curr_sum < target:
            left += 1
        else:
            return [left + 1, right + 1]


if __name__ == '__main__':
    n1 = [2, 7, 11, 15]
    t1 = 9  # [1,2] or [0,1]

    n2 = [2, 3, 4]
    t2 = 6  # [1,3] or [0,2]

    n3 = [-1, 0]
    t3 = -1  # [1,2] or [0,1]

    n4 = [1, 3, 4, 5, 7, 10, 11]
    t4 = 9  # [3,4] or [2,3]

    print(two_sum(n1, t1))  # [1,2] or [0,1]
    print(two_sum(n2, t2))  # [1,3] or [0,2]
    print(two_sum(n3, t3))  # [1,2] or [0,1]
    print(two_sum(n4, t4))
