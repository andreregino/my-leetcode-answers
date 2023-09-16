class Solution:
    def finalString(self, s: str) -> str:
        final_string = ""
        for i, letter in enumerate(s):
            if letter == "i":
                final_string = final_string[::-1]
            else:
                final_string += s[i]
            
        return final_string