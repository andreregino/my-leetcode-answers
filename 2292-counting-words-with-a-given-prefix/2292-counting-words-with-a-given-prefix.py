class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        prefix_size = len(pref)
        count = 0
        for word in words:
            if word[0:prefix_size] == pref:
                count+=1
        return count