class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end_string = True
        length = 0
        for k in range(len(s) -1, -1, -1):
            if s[k] == " " and end_string == True:
                continue
            elif s[k] != " ":
                length += 1
                end_string = False
            else:
                break
        return length
