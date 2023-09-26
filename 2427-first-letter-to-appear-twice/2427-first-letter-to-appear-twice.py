class Solution:
    def repeatedCharacter(self, s: str) -> str:
        dict_letters = {}
        for letter in s:
            if letter not in dict_letters:
                dict_letters[letter] = 1
            else:
                return letter

        