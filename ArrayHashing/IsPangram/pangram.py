

def is_pangram(pangram):
    ret = ""

    for sentence in pangram:
        letters = set()

        for char in sentence:
            letters.add(char)

        letters.discard(' ')

        if len(letters) == 26:
            ret += '1'
        else:
            ret += '0'

    return ret


t1 = ["pack my box with five dozen liquer jugs", "this is not a pangram"]  # '10'

print(is_pangram(t1))
