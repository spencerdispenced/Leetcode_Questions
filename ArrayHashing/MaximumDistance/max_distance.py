
# Find max distance betwwen same elements in array

def max_distance(nums):
    # Time: O(n)
    max_distance = 0
    uniques = {}

    for i in range(len(nums)):
        if nums[i] not in uniques:
            uniques[nums[i]] = i
        else:
            # current_distance = i - uniques.get(nums[i])
            # if current_distance > max_distance:
            #     max_distance = current_distance
            max_distance = max(max_distance, i - uniques.get(nums[i]))

    return max_distance


if __name__ == '__main__':
    nums = [3, 2, 1, 2, 1, 4, 5, 4, 2]  # 7
    print(max_distance(nums))

    nums2 = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]  # 10
    print(max_distance(nums2))
