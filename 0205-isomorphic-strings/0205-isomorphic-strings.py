class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_s_t = {}
        if len(set(s)) != len(set(t)):
            return False
        for index, letter in enumerate(s):
            if letter not in map_s_t:
                map_s_t[letter] = t[index]
            else:
                if map_s_t[letter] != t[index]:
                    return False
        
        return True
        