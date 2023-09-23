

# https://leetcode.com/problems/valid-palindrome-ii/


def is_palindrome(str, left, right):
    while left < right:
        if str[left] != str[right]:
            return False
        left += 1
        right -= 1
    return True


def is_palindrome_with_1_removal(str):
    # reversed_str = str[::-1]
    # if str == reversed_str:
    #     return True

    if len(str) == 0:
        return "Empty string"

    if len(str) < 2:
        return True

    left = 0
    right = len(str) -1

    if is_palindrome(str, left, right):
        return True

    while left < right:
        if str[left] == str[right]:
            left += 1
            right -= 1
        else:
            return is_palindrome(str, left+1, right) or is_palindrome(str, left, right-1)
    return True


if __name__ == '__main__':
    s = "aba"
    s2 = "abca"
    s3 = "abc"
    s4 = "a"
    s5 = ""
    print(is_palindrome_with_1_removal(s))  # True
    print(is_palindrome_with_1_removal(s2))  # True
    print(is_palindrome_with_1_removal(s3))  # False
    print(is_palindrome_with_1_removal(s4))  # True
    print(is_palindrome_with_1_removal(s5))  # Empty string

    