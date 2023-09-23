

# https://leetcode.com/problems/permutation-in-string/


"""

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Input: s1 = "ab", s2 = "eidboaoo"
Output: false

"""


def perm_in_string(s1, s2):
    # Time: O(26 * n)
    # Runtime 63 ms Beats 88.41%
    # Memory 14.1 MB Beats 23.49%

    if len(s1) > len(s2):
        return False

    s1Count = [0] * 26
    s2Count = [0] * 26

    # initial values for first set of window
    for i in range(len(s1)):
        s1Count[ord(s1[i]) - ord('a')] += 1
        s2Count[ord(s2[i]) - ord('a')] += 1

    left = 0
    for right in range(len(s1), len(s2)):
        if s1Count == s2Count:
            return True

        # increase introduced char count
        s2Count[ord(s2[right]) - ord('a')] += 1

        # reduce leaving char count
        s2Count[ord(s2[left]) - ord('a')] -= 1

        # Increment left pointer
        left += 1

    return s1Count == s2Count


def perm_in_string_optimized(s1, s2):
    # Time: O(n), Space: O(1)
    # Runtime 70 ms Beats 77.89%
    # Memory 14 MB Beats 59.75%

    if len(s1) > len(s2):
        return False

    s1_count, s2_count = [0] * 26, [0] * 26

    # Update char counts for initial window
    for i in range(len(s1)):
        s1_count[ord(s1[i]) - ord('a')] += 1
        s2_count[ord(s2[i]) - ord('a')] += 1

    # Check matches in initial arrays
    matches = 0
    for i in range(26):
        if s1_count[i] == s2_count[i]:
            matches += 1

    # Check rest of string with sliding window
    left = 0
    for right in range(len(s1), len(s2)):
        if matches == 26:
            return True

        # Increment from right side of window
        # Find index corresponding to current letter
        index = ord(s2[right]) - ord('a')
        s2_count[index] += 1  # Increment in count array

        # If there is now a match, Increment matches
        if s1_count[index] == s2_count[index]:
            matches += 1

        # If there was a match and incrementing caused it to not match anymore,
        #     decrement matches
        elif s1_count[index] + 1 == s2_count[index]:
            matches -= 1

        # Decrement count of letter at left side of window
        index = ord(s2[left]) - ord('a')
        s2_count[index] -= 1

        # If decrementing count caused a match, Increment matches
        if s1_count[index] == s2_count[index]:
            matches += 1

        # If decrementing count caused a mismatch, decrement matches
        elif s1_count[index] - 1 == s2_count[index]:
            matches -= 1

        # Contract window on left side by incrementing right pointer
        left += 1

    # Check matches after last iteration of loop
    return matches == 26


if __name__ == '__main__':
    str1 = "ab"
    test1 = "eidbaooo"  # True
    test2 = "eidboaoo"  # false

    str2 = "hello"
    test3 = "ooolleoooleh"  # False

    str3 = "hello"
    test4 = "ooollehooleh"

    # print(perm_in_string(str1, test1))  # True
    # print(perm_in_string(str1, test2))  # False
    # print(perm_in_string(str2, test3))  # False

    print(perm_in_string_optimized(str1, test1))  # True
    print(perm_in_string_optimized(str1, test2))  # False
    print(perm_in_string_optimized(str2, test3))  # False
    print(perm_in_string_optimized(str3, test4))  # True
