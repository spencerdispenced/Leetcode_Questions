

# https://leetcode.com/problems/evaluate-reverse-polish-notation/


# You are given an array of strings tokens that represents
# an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer
# that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression
# in a reverse polish notation.
# The answer and all the intermediate calculations
# can be represented in a 32-bit integer.


from collections import deque


def is_rev_polish(tokens: list[str]) -> int:
    # Time: O(n), Space: O(n)
    stack = deque()

    for c in tokens:
        if c == '+':
            stack.append(stack.pop() + stack.pop())

        elif c == '-':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(num2 - num1)

        elif c == '/':
            num1 = stack.pop()
            num2 = stack.pop()
            stack.append(int(num2 / num1))

        elif c == '*':
            stack.append(stack.pop() * stack.pop())

        else:
            stack.append(int(c))

    return stack[0]


if __name__ == '__main__':
    tokens1 = ["2", "1", "+", "3", "*"]
    print(is_rev_polish(tokens1))
    # Output: 9
    # Explanation: ((2 + 1) * 3) = 9

    tokens2 = ["4", "13", "5", "/", "+"]
    print(is_rev_polish(tokens2))
    # Output: 6
    # Explanation: (4 + (13 / 5)) = 6

    tokens3 = ["10", "6", "9", "3", "+", "-11",
               "*", "/", "*", "17", "+", "5", "+"]
    print(is_rev_polish(tokens3))
    # Output: 22
    # Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
    # = ((10 * (6 / (12 * -11))) + 17) + 5
    # = ((10 * (6 / -132)) + 17) + 5
    # = ((10 * 0) + 17) + 5
    # = (0 + 17) + 5
    # = 17 + 5
    # = 22
