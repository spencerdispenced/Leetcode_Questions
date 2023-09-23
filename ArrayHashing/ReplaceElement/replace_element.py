
# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/


# Given an array arr, replace every element in that array with the greatest element among the elements to its right,
# and replace the last element with -1.

# After doing so, return the array.

# def replace_elements(arr: list[int]) -> list[int]:
#     # Time: O(n)
#     if len(arr) <= 1:
#         return [-1]
    
#     curr_max = arr[-1]
#     for i in range(len(arr)-2, -1, -1):
#         if arr[i] > curr_max:
#             temp  = curr_max
#             curr_max = arr[i]
#             arr[i] = temp
#         else:
#             arr[i] = curr_max
#     arr[-1] = -1

#     return arr

def replace_elements(arr: list[int]) -> list[int]:
    # Time: O(n)
    maxNum = -1
    for i in range(len(arr) -1, -1, -1):
        newMax = max(maxNum, arr[i])
        arr[i] = maxNum
        maxNum = newMax

    return arr
            

if __name__ == '__main__':
    nums1 = [17,18,5,4,6,1] # [18,6,6,6,1,-1]
    nums2 = [400] # -1
    print(replace_elements(nums1))
    print(replace_elements(nums2))
