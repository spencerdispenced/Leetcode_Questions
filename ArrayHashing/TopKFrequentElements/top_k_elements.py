
# https://leetcode.com/problems/top-k-frequent-elements/


"""
1. Create a hashmap 'count' for counts of each number, key: num, val: count, <num : count>

   Create an array 'frequency' of arrays of size of length of input array. [ [], [], [], [] ]
        - Each index of array corresponds to frequency of nums in input list
        - Max frequency is if all nums in input list are the same
        - [1,1,1,2,2,3] -> [ [3], [2], [1], [], [], [] ]
        - [1,1,1,2,2,2,3,3] -> [ [], [3], [1,2], [], [], [], [], [] ]

    Create array to store result

2. Iterate over nums in input list:

    2.1: Increment value of key 'num' in 'count' hashmap


3. Iterate over items (num: count) in 'counts' hashmap:

    3.1: In 'frequency' array, at index 'count', append 'num' to sublist


4. Iterate over 'frequency' array backwards, starting with last element:

    4.1: Iterate over subarray:

        5. Append num to result array

        6. After appending, check if length of result array is equal to 'k'

            If so: return result array

"""


def top_k_frequent(nums: list[int], k: int) -> list[int]:
    # Time: O(n+n) or just O(n)
    counts = {}
    # init list of lists in size nums
    freq = [[] for i in range(len(nums) + 1)]

    res = []

    # count each occurance of number, {value: count}
    for number in nums:
        counts[number] = 1 + counts.get(number, 0)

    for number, count in counts.items():
        # at index 'frequency', insert 'value' of occurance into list
        freq[count].append(number)

    # iterate through list backwards, value of highest indexes get appended first
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            # when len of result is same as top k, return
            if len(res) == k:
                return res


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(top_k_frequent(nums, k))

    nums2 = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3]
    k2 = 2
    print(top_k_frequent(nums2, k2))

    nums3 = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
    k3 = 2
    print(top_k_frequent(nums3, k3))
