class Solution:
    def replaceDigits(self, s: str) -> str:
        final_string = ""
        for i, letter_number in enumerate(s):
            if i % 2 == 1:
                final_string += chr(int(ord(s[i-1])) + int(letter_number))
            else:
                final_string += letter_number
        return final_string

