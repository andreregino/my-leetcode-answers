class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        last_int = -999999
        s = s.split()
        for word in s:
            if word.isdigit():
                if int(word) > last_int:
                    last_int = int(word)
                else:
                    return False
        return True