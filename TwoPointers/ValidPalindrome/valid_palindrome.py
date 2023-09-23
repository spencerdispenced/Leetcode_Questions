

# https://leetcode.com/problems/valid-palindrome/


"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.


Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.


Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.


Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.


1. Set left pointer to begining of string, right pointer to end of string

2. Loop while Left doesn't meet right (while l < r):

    2.1: Check if value at left pointer is not alphanumeric:
         If not alphanumeric: -Increment left pointer
                              -Repeat (continue) loop

    2.2: Check if value at right pointer is not alphanumeric:
         If not alphanumeric: -Decrement right pointer
                              -Repeat (continue) loop

    2.3: Check that values at left pointer and right pointer are not exactly equal (Convert to lower case):

         If not equal: Return false

    2.4: -Increment left pointer
         -Decrement right pointer


3. Default of return true if not returned false in loop

"""


def is_palindrome(str):
    new_str = ''

    for c in str:
        if c.isalnum():
            new_str += c.lower()

    return new_str == new_str[::-1]


def is_palindrome_two(str):
    # Time: O(n), Space: O(1)
    left = 0
    right = len(str)-1

    while left < right:
        # increment from each side until an alphanumeric character
        if not str[left].isalnum():
            left += 1
            continue
        if not str[right].isalnum():
            right -= 1
            continue

        # Check if character on either side matches
        if str[left].lower() != str[right].lower():
            return False

        left += 1
        right -= 1

    return True


def alphaNum(c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))


if __name__ == '__main__':
    s = "A man, a plan, a canal: Panama"
    s2 = "race a car"
    print(is_palindrome(s))  # True
    print(is_palindrome(s2))  # False

    print(is_palindrome_two(s))
    print(is_palindrome_two(s2))
