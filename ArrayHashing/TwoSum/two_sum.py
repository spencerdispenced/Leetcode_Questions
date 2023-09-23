# [2,7,12,15,10]    9

# given array and target, find indexes that return target

# https://leetcode.com/problems/two-sum/


"""
1. Create hashmap for already checked values with index: <val, index>

2. Iterate over nums list:

    3. Inside loop: Take target - current num, store in variable 'diff'

    4. Check if 'diff' value is already stored in hashmap

        If so: Grab index of 'diff' from hashmap
               Return 'diff' index with current index as a list

        Else: Store current value and index in hashmap
              Continue loop

5. Return default values in list if two sum not found


"""


def find_indexes_brute(nums, target):
    # Time: O(n^2)
    # Space: O(1)
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def find_index(nums, target):
    # Time: O(n)
    # Space: O(n)

    prev_map = {}  # val : index

    for index, num in enumerate(nums):
        diff = target - num
        if diff in prev_map:
            return [prev_map[diff], index]
        prev_map[num] = index
    return []


arr1 = [10, 7, 2, 15, 1]
arr2 = [2, 5, 5, 1]


# print(find_indexes_brute(arr1, 17))
# print(find_indexes_brute(arr1, 9))
# print(find_indexes_brute(arr1, 25))
# print(find_indexes_brute(arr1, 16))
# print(find_indexes_brute(arr1, 100))

# print(find_indexes_brute(arr2, 10))


print(find_index(arr1, 17))
print(find_index(arr1, 9))
print(find_index(arr1, 25))
print(find_index(arr1, 16))
print(find_index(arr1, 100))
print(find_index(arr2, 10))
