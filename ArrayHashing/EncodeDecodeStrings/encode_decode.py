

# https://www.lintcode.com/problem/659/


"""
Encode:

    1. Create empty string variable 'Encoded'

    2. Loop over strings in input list, For each word in list:
        - Build the encoded string
        2.1: Take length of current word, add to 'Encoded'
             Add '#' symbol - used to delimit subsegments
             Add current word

Decode:
    1. Initialize variable 'i' to 0
       Create empty 'Decoded' array

    2. Loop over entire encoded string (i < length of encoded):

        2.1 initialize variable 'j' to 'i'

        3. Loop over subsegment, until delimter reached (encoded[j] != '#'):

            3.1: Increment 'j'

        4. Get length of substring (length of array slice [i:j])

            - This will find the length of word added during encoding,
                not including delimiter

        5. Get substring slice
            - First value is j + 1,  moves first value off delimiter
            - Second value is j + 1 + length, end of substring

        6. Append substring to 'Decoded' list

        7. Update 'i' to latest position of substring, j + 1 + length



"""


class EncodeDecode:

    def __init__(self, strs: list[str]) -> None:
        self.strs = strs
        self.encoded = ''
        self.decoded = []

    def encode(self):
        for s in self.strs:
            self.encoded += str(len(s)) + "#" + s

    def decode(self):
        i = 0

        while i < len(self.encoded):
            j = i
            while self.encoded[j] != '#':
                j += 1

            length = int(self.encoded[i:j])

            self.decoded.append(self.encoded[j + 1: j + 1 + length])

            i = j + 1 + length

    def show_encoded(self):
        print(self.encoded)

    def show_decoded(self):
        print(self.decoded)


if __name__ == '__main__':
    strs = ['lint', 'code', 'love', 'you']

    test = EncodeDecode(strs)
    test.encode()
    test.show_encoded()
    test.decode()
    test.show_decoded()
