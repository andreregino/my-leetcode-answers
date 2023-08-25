class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ""
        first_string = strs[0]
        if len(strs) == 1 and len(strs[0]) != 0:
            return strs[0]
        min_len = len(min(strs, key=len))
        for j in range(min_len): # j = caracter de cada str
            add = False
            for i in range(1, len(strs)): # i = cada str
                if strs[i][j] == first_string[j]:
                    add = True
                else:
                    add = False
                    break
            if add:
                longest_prefix += first_string[j]
            else:
                break
        return longest_prefix                


