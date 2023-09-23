

# https://leetcode.com/problems/longest-consecutive-sequence/description/


"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.


Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.



1. Create set of nums from input list
   Initialize max_sequence variable to 0

2. Iterate over nums set:

    2.1 Check if current number - 1 is not present in nums set
        - if so, it means beginning of sequence
           - initialize sequence variable to 0

    3. Loop while current number + sequence is present in nums set
        
        3.1: Increment sequence variable

    4. Check if current sequence is greater than max sequence, update if so

5. return max sequence




"""


def find_max_concequtive_sequence(nums: list) -> int:
    # Time: O(n), Space O(n)
    nums_set = set(nums)

    max_sequence = 0
    for number in nums_set:
        if number - 1 not in nums_set:
            sequence = 0
            while number + sequence in nums_set:
                sequence += 1
            max_sequence = max(max_sequence, sequence)
    return max_sequence


if __name__ == '__main__':
    nums = [100, 4, 200, 1, 3, 2]
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]

    print(find_max_concequtive_sequence(nums))  # 4
    print(find_max_concequtive_sequence(nums2))  # 9
