class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteCopy = ransomNote

        for ransom_letter in ransomNote:
            if ransom_letter not in magazine:
                return False
            else:
                magazine = magazine.replace(ransom_letter, "", 1)
        return True
