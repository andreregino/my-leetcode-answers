class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        line_1 = "qwertyuiop"
        line_2 = "asdfghjkl"
        line_3 = "zxcvbnm"
        selected_words = []
        
        for word in words:
            count_1 = 0
            count_2 = 0
            count_3 = 0
            for w in word.lower():
                if w in line_1:
                    count_1 += 1
                elif w in line_2:
                    count_2 += 1
                elif w in line_3:
                    count_3 += 1
                else:
                    break
            
            if count_1 == len(word) or count_2 == len(word) or count_3 == len(word):
                selected_words.append(word)
        return selected_words