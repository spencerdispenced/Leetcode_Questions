

#  https://leetcode.com/problems/longest-repeating-character-replacement/


"""
You are given a string s and an integer k. 
You can choose any character of the string and change it to any other uppercase English character.
 You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.


Sliding window, expand window until it is no longer valid. A window is
valid if the number of replacements needed is less than or equal to allowed 
swaps. If the window is invalid, contract from the left until it is. keep track 
of largest valid window found until all characters have been checked.

To find number of replacements needed:
    1. Find window size
    2. substract value of maximum occuring characters

Time: O(n)
Space: O(26)


1. Create Hashmap to store character counts
   Set left and right pointer to 1st index
   Create variable to store max valid window size

2. Start expanding window, loop right pointer to end of string:

    2.1: Increment the count of the current character in Hashmap

    3. Check if current window is valid:

        3.1: Windows size = right pointer index - left pointer index

             Replacements needed = window size - maximum of counts in Hashmap

             Valid if replacements needed is less than or equal to 'k'

    4. Loop while NOT valid:

        4.1: -Decrement the count of value at left pointer from hashmap

             -Increment left pointer

    5. Once the window is valid again, check if current window size is greater
        than stored size, update if necessary

6. Return max window size

"""


def character_replacement_optimized(s: str, k: int) -> int:

    # Runtime 112ms Beats 88.47% Memory 14MB Beats 52.29%
    count = {}
    res = 0

    left = 0
    max_freq = 0  # optimization
    for right in range(len(s)):
        count[s[right]] = 1 + count.get(s[right], 0)

        # update max_freq to either current or newly added char
        max_freq = max(max_freq, count[s[right]])

        if (right - left + 1) - max_freq > k:
            count[s[left]] -= 1
            left += 1

        res = max(res, right - left + 1)
    return res


def character_replacement(s: str, k: int) -> int:
    # Time: O(26 * n) or O(n)
    # Runtime 174ms Beats 52.11% Memory 14.1MB Beats 14.65%

    count = {}
    res = 0
    left = 0

    for right in range(len(s)):
        # Increment count of letter
        count[s[right]] = 1 + count.get(s[right], 0)

        # check if window is valid,
        # window size (left-right + 1) - max char count
        #  is equal to the number of replacements needed, check
        #  if greater than k (invalid window)
        while (right - left + 1) - max(count.values()) > k:
            # decrement count of char at left pointer
            count[s[left]] -= 1

            # move left pointer
            left += 1

        res = max(res, right - left + 1)

    return res


if __name__ == '__main__':
    s1 = "ABAB"
    k1 = 2  # 4

    s2 = "AABABBA"
    k2 = 1  # 4

    s3 = "ABABBA"
    k3 = 2  # 5

    print(character_replacement(s1, k1))
    print(character_replacement(s2, k2))
    print(character_replacement(s3, k3))
