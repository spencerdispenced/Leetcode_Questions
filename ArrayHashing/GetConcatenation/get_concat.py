
# https://leetcode.com/problems/concatenation-of-array/

# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.

# Return the array ans.


def get_concatenation(nums: list[int]) -> list[int]:
    ret = []
    for i in range(2):
        for num in nums:
            ret.append(num)
    return ret

if __name__ == '__main__':
    nums1 = [1,2,1] #[1,2,1,1,2,1]
    nums2 = [1,3,2,1] #[1,3,2,1,1,3,2,1]
    print(get_concatenation(nums1))
    print(get_concatenation(nums2))