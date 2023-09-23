

def max_non_adj_sum(nums):
    prev_max = 0
    curr_max = 0

    for i in nums:
        new_max = max(prev_max + i, curr_max)
        prev_max = curr_max
        curr_max = new_max

    return curr_max


if __name__ == '__main__':
    nums = [1, 2, 3, 1]  # 4
    nums2 = [2, 7, 9, 3, 1]  # 12
    nums3 = [3, 2, 7, 10]  # 13

    print(max_non_adj_sum(nums))
    print(max_non_adj_sum(nums2))
    print(max_non_adj_sum(nums3))
