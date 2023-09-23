

# https://leetcode.com/problems/valid-parentheses/

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

# def is_valid_parentheses(s: str) -> bool:
#     # Time: O(n), Space: O(n)

#     stack = []
#     close_to_open = {')': '(',  ']': '[',  '}': '{'}

#     for c in s:
#         if c in close_to_open:
#             if stack and stack[-1] == close_to_open[c]:
#                 stack.pop()
#             else:
#                 return False
#         else:
#             stack.append(c)

#     return True if not stack else False


def is_valid_parentheses(s: str) -> bool:
    # Time: O(n), Space: O(n)

    stack = []
    close_to_open = {')': '(',  ']': '[',  '}': '{'}

    for c in s:
        if c not in close_to_open:  # opening paren
            stack.append(c)
            
        # if closing paren and top of stack is matching opening paren
        elif stack and stack[-1] == close_to_open[c]:
            stack.pop()
            
    return True if not stack else False


if __name__ == '__main__':
    s1 = "()"
    s2 = "()[]{}"
    s3 = "(]"
    s4 = "([)]"
    s5 = "([])"

    print(is_valid_parentheses(s1))  # True
    print(is_valid_parentheses(s2))  # True
    print(is_valid_parentheses(s3))  # False
    print(is_valid_parentheses(s4))  # False
    print(is_valid_parentheses(s5))  # True
