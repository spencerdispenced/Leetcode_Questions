
# https://leetcode.com/problems/is-subsequence/

# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
# of the characters without disturbing the relative positions of the remaining characters.
# (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

#
def is_subsequence(s: str, t: str) -> bool:
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)

if __name__ == '__main__':
    s1 = "abc"
    t1 = "ahbgdc"  # True

    s2 = "axc"
    t2 = "ahbgdc"  # False
    print(is_subsequence(s1, t1))
    print(is_subsequence(s2, t2))