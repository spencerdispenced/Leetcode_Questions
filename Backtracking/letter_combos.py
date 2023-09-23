
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/


def letter_combinations(digits: str) -> list[str]:
    # TimeL O(n * 4^n)
    ret = []
    digitToChar = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "qprs",
        "8": "tuv",
        "9": "wxyz"
    }

    def backtrack(i, curr_str):
        if len(curr_str) == len(digits):
            ret.append(curr_str)
            return

        for c in digitToChar[digits[i]]:
            backtrack(i + 1, curr_str + c)

    if digits:
        backtrack(0, "")

    return ret


if __name__ == '__main__':
    digits1 = "23"
    # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    print(letter_combinations(digits1))

    digits2 = ""
    print(letter_combinations(digits2))  # []

    digits3 = "2"
    print(letter_combinations(digits3))  # ["a","b","c"]
