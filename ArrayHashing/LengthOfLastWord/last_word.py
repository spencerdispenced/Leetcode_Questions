

# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal
# substring
# consisting of non-space characters only.



def last_word_length(s):
    count = 0
    for i in range(len(s)-1, -1, -1): 
        if s[i] == ' ':
            if count >= 1:
                return count
        else:
            count += 1
    return count


if __name__ == '__main__':
    s = "Hello World"
    print(last_word_length(s))  # 5

    s2 = "   fly me   to   the moon  "
    print(last_word_length(s2))  # 4

    s3 = "luffy is still joyboy"
    print(last_word_length(s3))  # 6
