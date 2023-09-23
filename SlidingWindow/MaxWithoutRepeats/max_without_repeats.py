

# https://leetcode.com/problems/longest-substring-without-repeating-characters/


"""
Given a string s, find the length of the longest
substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.


Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.


Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


Sliding window. Window expands until a duplicate is found, constracts if duplicate


1. Create empty set
   Set left pointer to 1st index
   Set right pointer to 1st index
   Create variable to store output, max substring length

2. Loop right pointer over string:

    2.1: Check if current char is already in set:

        If not: -Add to set
                -Update max substring length if current set
                      length is greater than stored max length

        If duplicate: 

            3. Iterate left pointer over string, removing chars from set,
                       until 1st occurance of duplicate removed

4. Return max substring length

"""


def longest_substring(s: str) -> int:
    # Time: O(n), Space: O(n)
    # 76 ms Beats 51.83%, Memory 14MB Beats 45.41%
    chars = set()
    l = 0
    res = 0

    for r in range(len(s)):
        while s[r] in chars:
            chars.remove(s[l])
            l += 1
        chars.add(s[r])
        res = max(res, len(chars))
    return res


if __name__ == '__main__':
    s1 = "abcabcbb"
    s2 = "bbbbb"
    s3 = "pwwkew"
    s4 = "aab"

    print(longest_substring(s1))  # 3
    print(longest_substring(s2))  # 1
    print(longest_substring(s3))  # 3
    print(longest_substring(s4))  # 2
