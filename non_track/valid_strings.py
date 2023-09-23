
"""
Given 3 strings as the input, check if the 3rd string is valid. The 3rd String is valid if:

1.) Frequency of each character in the 3rd string should be less than or equal to the sum of 
    frequency of that character in first 2 strings.

2.) Source index of a character is the position where the character appears in first two strings. 
    If the character appears in both string, then the highest position will become the source index. 
    If the character appear more than once in a string then the highest position is considered. 
    Pace the source index for all characters in 3rd string. Assume the index starts with zero. 
    The source index should be in ascending order.

If above two conditions match, 3rd string is valid and print output as 1. Else print output as 0.

Note: Perform case-sensitive match



rkpesh#@, mdn, rmde#@ = pass

rkpesh#@, mdn, rdme#@ - fail, source indexes not acending

rkpesh, mdn, rxdy - fail, 1st cond not med

exAmple, Template, temperature - fail, 1st cond not met

"""


def get_char_freq(strs: list[str]) -> dict[str:int]:
    freq = {}
    for str in strs:
        for char in str:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
    return freq


def check_freq(freq1: dict[str:int], freq3: dict[str:int]) -> bool:
    for char, count in freq3.items():
        if char not in freq1:
            return False
        if count > freq1[char]:
            return False

    return True


def get_highest_indexes(strs: list[str]) -> dict[str:int]:
    # get dict with value: highest index
    highest_indexes = {}
    for str in strs:
        highest_indexes.update({index: char for char, index in enumerate(str)})

    return highest_indexes


def check_acending_order(highest_indexes: dict[str:int], third_str: str) -> bool:

    prev_index = 0
    for index in third_str:
        current_index = highest_indexes.get(index)
        if current_index is None or current_index < prev_index:
            return False
        else:
            prev_index = current_index

    return True


def check_valid_string(strs: str) -> int:
    # Split input string into list of first two and third
    strings = strs.split(',')
    first_two = [strings[0], strings[1]]
    third = strings[2]

    # get char frequencies from first two strings and third separatly, pass 3rd as list
    first_two_freq = get_char_freq(first_two)
    third_freq = get_char_freq([third])

    # Get highest occuring indexes of chars in first two strings
    highest_indexes = get_highest_indexes(first_two)

    # Check both frequencies and acending order are valid
    if check_freq(first_two_freq, third_freq) and check_acending_order(highest_indexes, third):
        return True
    else:
        return False


if __name__ == '__main__':
    input1 = "rkpesh#@,mdn,rmde#@"  # pass
    input2 = "rkpesh#@,mdn,rdme#@"  # fail, source indexes not acending
    input3 = "rkpesh,mdn,rxdy"  # fail, 1st cond not med
    input4 = "exAmple,Template,temperature"  # fail, 1st cond not met
    input5 = "spencer,boss,bpnr"

    print(check_valid_string(input1))
    print(check_valid_string(input2))
    print(check_valid_string(input3))
    print(check_valid_string(input4))
    print(check_valid_string(input5))
