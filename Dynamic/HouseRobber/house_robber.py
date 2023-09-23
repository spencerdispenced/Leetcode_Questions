
# https://leetcode.com/problems/house-robber/


# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint stopping you
# from robbing each of them is that adjacent houses have security systems connected 
# and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.

def rob(nums):
    # Handle edge case
    if len(nums) < 2:
        return nums[0]
    # Create array to store max at each index
    max_loot = [0] * len(nums)

    # Set first to indexes to potential maxes
    max_loot[0] = nums[0]
    max_loot[1] = max(nums[0], nums[1])

    # loop over rest of array, starting at idx 2
    # Max loot at current index is either current idx + max_loot from 2nd index previous,
    #  or only max_loot from previous index  
    # Recurrence relation: max_loot[i] = max(max_loot[i-2] + nums[i], max_loot[i-1])
    for i in range(2, len(nums)):
        max_loot[i] = max(max_loot[i-2] + nums[i], max_loot[i-1])

    # total potential max loot will progrss to end of array
    return max_loot[-1]


if __name__ == '__main__':
    nums = [1,2,3,1]
    nums2 = [2,7,9,3,1]
    print(rob(nums))  # 4
    print(rob(nums2))  # 12
