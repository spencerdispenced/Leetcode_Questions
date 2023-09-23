
# https://leetcode.com/problems/valid-anagram/


""" 
1. Check that length of both strings matches

2. Count all occurances of each letter in both strings
    - Store in separate hashmap for each string, <char, count>

 3. Iterate over one of the hashmaps, check the count against
    the values in the other hashmap, must be exactly equal
"""


def valid_anagram(s, t):
    # Time: O(s + t)
    # Space: O(s + t)
    # return Counter(s) == Counter(t)
    # return sorted(s) == sorted(t) O(1) space complexity

    if len(s) != len(t):
        return False

    count_s = {}
    count_t = {}

    for i in range(len(s)):
        count_s[s[i]] = 1 + count_s.get(s[i], 0)
        count_t[t[i]] = 1 + count_t.get(t[i], 0)

    return True if count_s == count_t else False

    # for c in count_s:
    #     if count_s[c] != count_t.get(c, 0):
    #         return False

    # return True


if __name__ == '__main__':
    test1 = 'anagram'
    test2 = 'nagaram'
    test3 = 'apple'
    test4 = 'ppale'
    test5 = 'apple'
    test6 = 'ppalx'
    print(valid_anagram(test1, test2))
    print(valid_anagram(test3, test4))
    print(valid_anagram(test5, test6))
