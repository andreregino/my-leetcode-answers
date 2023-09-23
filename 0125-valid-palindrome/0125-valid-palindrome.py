class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""
        letter_dict = {
            "0": 0,
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0,
            "7": 0,
            "8": 0,
            "9": 0,
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0,
            "e": 0,
            "f": 0,
            "g": 0,
            "h": 0,
            "i": 0,
            "j": 0,
            "k": 0,
            "l": 0,
            "m": 0,
            "n": 0,
            "o": 0,
            "p": 0,
            "q": 0,
            "r": 0,
            "s": 0,
            "t": 0,
            "u": 0,
            "v": 0,
            "w": 0,
            "x": 0,
            "y": 0,
            "z": 0
        }
        for letter in s.lower():
            if letter in letter_dict:
                new_string += letter
        
        if len(new_string) == 0 or len(new_string) == 1:
            return True

        for i in range(0, len(new_string)//2):
            if new_string[i] != new_string[-i-1]:
                return False
        return True