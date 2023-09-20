class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = 0
        for each_letter in s:
            if each_letter == letter:
                count+=1
        return int((count/len(s)) * 100)