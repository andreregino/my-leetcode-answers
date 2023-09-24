class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        count = 0
        list_vowels = ["a", "e", "i", "o", "u"]
        for i in range(left, right+1):
            if words[i][0] in list_vowels and words[i][-1] in list_vowels:
                count+=1

        return count