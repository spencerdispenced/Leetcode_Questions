
# https://leetcode.com/problems/maximum-number-of-balloons/S


"""
1. Create a hashmap with each letter of 'balloon' ('balon'), with 
    default values of 0 for each

2. Iterate over input string

    If current letter is in hashmap, increment letter value.

    Else ignore

3. After loop: for keys 'l' and 'o', floor/integer divide value by 2

4. Return the minimum value from hashmap, will correspond to maximum
    possible occurance of 'balloon'
    
"""


def find_max_balloons(str):
    ballons = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}

    # increment count f0r each matching letter of balloon and str
    for letter in str:
        if letter.lower() in ballons:
            ballons[letter] += 1

    # floor div on 'l', and 'o' to match equivalence with other lettes
    ballons['l'] //= 2
    ballons['o'] //= 2

    # min value in dict will be min occurances of 'balloon'
    return min(ballons.values())


if __name__ == '__main__':
    test1 = "nlaebolko"  # 1
    test2 = "loonbalxballpoon"  # 2
    test3 = "leetcode"  # 0
    test4 = 'balon'

    print(find_max_balloons(test1))
    print(find_max_balloons(test2))
    print(find_max_balloons(test3))
    print(find_max_balloons(test4))
