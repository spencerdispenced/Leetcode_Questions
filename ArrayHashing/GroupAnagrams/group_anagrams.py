
from collections import defaultdict


# https://leetcode.com/problems/group-anagrams/


"""
1. Create hashmap with key as list of chars, value as list of strings
    - or create hashmap of key string, value list of strings <string, list<string>>
    - or create array of array of strings <list<list<string>>

2. Iterate over each word in input list:

    2.1: Create a char array of length 26, index will correspond to letter of alphabet
            - idx 0: 'a', idx 5: 'e', etc

    3. Iterate over each letter of current word:

        3.1: Get ascii value of current letter, subtract ascii value of 'a'
                to find appropriate index for letter in above char array
                - Ascii values are in order, so b(101) - a(100) = 1, 
                  or b corresponds to index 1 in above array
            
        3.2: Increment appropriate index in above array
            - Array will have letter counts for the current word with each
              index representing the letter and the value representing the count
            - Creates key for above hashmap
            - Depending on language, convert array to string

    4. Add word to above hashmap with exact letter count as key, append to list of values


5. Return values from hashmap

"""


def group_anagrams(strs):
    # Time: O(m * n)

    # mapping charCount to list of Anagrams
    res = defaultdict(list)

    for word in strs:
        # create list for each letter in alphabet
        count = [0] * 26

        # map letter to respective index, increment count of each letter
        # ascii is in order, 81 - 80 = 1, or index 1 for 'b'
        for char in word:
            count[ord(char) - ord('a')] += 1

        # add word as value corresponding to key with exact letter count
        res[tuple(count)].append(word)

    return res.values()


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]


if __name__ == '__main__':
    print(group_anagrams(strs))
