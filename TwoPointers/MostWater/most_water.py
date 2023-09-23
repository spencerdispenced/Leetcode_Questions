

# https://leetcode.com/problems/container-with-most-water/


"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7].
In this case, the max area of water (blue section) the container can contain is 49.


Input: height = [1,1]
Output: 1


1. Set left pointer to index 0
   Set right pointer to last index
   Create output variable

2. Loop until left pointer meets right pointer (while left < right):

    2.1: Calculate current area:
        - Width: right index minus left index
        - Lowest height: lowest value at either left or right pointer
        - area: width * height

    2.2: Check is current area is greater than stored max area, update if so

    - To potentially find the greatest area, the highest 'lowest height' needs to be found
      Do this by moving the pointer at the lower height at every iteration

    3. If left height is less than right height:
       - Increment left pointer

       Otherwise, Decrement right pointer

4. Return max area

"""


def max_area_brute(nums):
    # Time: O(n^2)
    res = 0

    for l in range(len(nums)):
        for r in range(l + 1, len(nums)):
            area = (r - l) * min(nums[l], nums[r])
            res = max(res, area)
    return res


def most_water(nums):
    left = 0
    right = len(nums) - 1

    area = 0
    while left < right:
        width = right - left
        lowest_height = min(nums[left], nums[right])
        curr_area = width * lowest_height

        area = max(area, curr_area)

        if nums[left] < nums[right]:
            left += 1
        else:
            right -= 1

    return area


if __name__ == '__main__':
    h1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]  # 49
    h2 = [1, 1]  # 1

    # print(max_area_brute(h1))
    # print(max_area_brute(h2))

    print(most_water(h1))
    print(most_water(h2))
