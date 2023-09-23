

# https://leetcode.com/problems/trapping-rain-water/


""""
Given n non-negative integers representing an elevation map where the width of each bar is 1,
 compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
In this case, 6 units of rain water (blue section) are being trapped.

Input: height = [4,2,0,3,2,5]
Output: 9


Given elevation map array, compute trapped water
    Ex. height = [0,1,0,2,1,0,1,3,2,1,2,1] -> 6

    2 pointers, outside in, track max left/right
    For lower max, curr only dependent on that one
    Compute height of these, iterate lower one

    Time: O(n)
    Space: O(1)



1. Create left pointer set to index 0
   Create right pointer set to last index
   Create leftMax variable set to value at left pointer
   Create rightMax variable set to value at right pointer
   Create output variable

2. Loop until pointers meet (while left < right):

    2.1: Check if leftMax is less or equal to rightMax:
         If so:
                2.2: -Increment left pointer
                     -Check if new left pointer value is greater than current leftMax, update if needed
                     -Add total value by LeftMax minus current left value

         Otherwise:
                2.3: -Decrement right pointer
                    -Check if new right pointer value is greater than current rightMax, update if needed
                    -Add total value by rightMax minus current right value

3. Return total

"""


def trap_water(height):
    # Time: O(n), Space: O(1)

    if not height:
        return 0

    left = 0
    right = len(height) - 1
    left_max = height[left]
    right_max = height[right]

    total = 0

    while left < right:
        if left_max <= right_max:
            left += 1
            left_max = max(left_max, height[left])
            total += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            total += right_max - height[right]

    return total


if __name__ == '__main__':
    h1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]  # 6
    h2 = [4, 2, 0, 3, 2, 5]  # 9

    print(trap_water(h1))
    print(trap_water(h2))
