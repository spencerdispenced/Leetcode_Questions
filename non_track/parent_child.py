

# Given two strings of equal length, whats the longest string that
# can be constructed such that it is a child of both?
# A string is a child of another string if it can be formed
# by deleting 0 or more characters from the other string
# Return length of longest child

# Ex: ABCD,ABDC -> 3  , 2 longest child strings possible
#   common to both: ABC and ABD


def longest_child(s1: str, s2: str) -> int:
    n, m = len(s1), len(s2)
    lcs = [[0]*(m+1) for i in range(n+1)]

    for i, c1 in enumerate(s1):
        for j, c2, in enumerate(s2):
            if c1 == c2:
                lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])

    return lcs[n-1][m-1]


if __name__ == '__main__':

    input_strings = "ABCD,ABDC".split(',')
    string1 = input_strings[0]
    string2 = input_strings[1]

    print(longest_child(string1, string2))
