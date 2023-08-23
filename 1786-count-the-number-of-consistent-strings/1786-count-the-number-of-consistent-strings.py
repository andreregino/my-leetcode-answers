class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            add = True
            for w in word:
                if w not in allowed:
                    add = False
                    
            if add:
                count+=1
        return count