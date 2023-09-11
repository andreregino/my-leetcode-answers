class Solution:
    def toLowerCase(self, s: str) -> str:
        final_string = ""

        for letter in s:
            if 65 <= ord(letter) <= 90:
                final_string += chr(ord(letter) + 32)
            else:
                final_string += letter

        return final_string