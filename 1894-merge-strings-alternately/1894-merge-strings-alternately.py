class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        max_length = 0
        final_string = ""
        len_1 = len(word1)
        len_2 = len(word2)
        if len_1 > len_2:
            max_length = len_1
        else:
            max_length = len_2


        for i in range(max_length):
            if i < len_1:
                final_string += word1[i]
            if i < len_2:
                final_string += word2[i]


        return final_string