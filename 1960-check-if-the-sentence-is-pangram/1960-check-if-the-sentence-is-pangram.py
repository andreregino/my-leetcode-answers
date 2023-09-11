class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters = {}
        for letter in sentence:
            if letter not in letters:
                letters[letter] = 1
            
        return len(letters) == 26