

# https://leetcode.com/problems/3sum/


"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k,
 and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.


Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.


Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.


Strategy: Sort the array, then for each item in array, try to solve twoSum 
          with remaining elements of array

1. Sort input array
   Create output array

2. Loop over sorted input array:
   
   2.1: If current value is same as previous value: skip

   2.2: Create left pointer set to next value in array
        Create right pointer set to last item in array

   3: Loop while pointers don't cross (while left < right):

      3.1: Find current sum by adding values at left and right pointers,
           and value at index in outer loop

      3.2: If current sum is greater than target: Decrement right pointer

           If current sum is less than target: Increment left pointer

           Else current sum equals target:
               - Append all three indicies to result array as an array
               - Increment left pointer
                  - Keep incrementing left pointer if value is the same as previous value

4. Return output array 


"""



def three_sum(nums):
    # 3 numbers from array that sum to 0
    # Time: O(nlogn) for sort, O(n^2) for traversal -> O(n^2)
    # Space: O(1) or O(n) depending on sort library
    res = []
    nums.sort()

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i-1]:  # not first value and not same as value before
            continue

        # Solve twoSum
        left = i + 1
        right = len(nums) - 1

        while left < right:
            curr_sum = a + nums[left] + nums[right]

            if curr_sum > 0:
                right -= 1
            elif curr_sum < 0:
                left += 1
            else:
                res.append([a, nums[left], nums[right]])
                left += 1
                while nums[left] == nums[left - 1] and left < right:
                    left += 1

    return res


if __name__ == '__main__':
    nums1 = [-1, 0, 1, 2, -1, -4]  # [[-1,-1,2],[-1,0,1]]

    nums2 = [0, 1, 1]  # []

    nums3 = [0, 0, 0]  # [[0,0,0]]

    nums4 = [-3, 3, 4, -3, 1, 2]  # [[-3, 1, 2]]

    print(three_sum(nums1))
    print(three_sum(nums2))
    print(three_sum(nums3))
    print(three_sum(nums4))
