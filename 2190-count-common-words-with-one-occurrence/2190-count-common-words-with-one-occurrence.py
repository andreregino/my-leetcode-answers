class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        dict_1 = {}
        dict_2 = {}

        for word1 in words1:
            if word1 not in dict_1:
                dict_1[word1] = 0
            dict_1[word1] = dict_1[word1] + 1
        
        for word2 in words2:
            if word2 not in dict_2:
                dict_2[word2] = 0
            dict_2[word2] = dict_2[word2] + 1
        
        for k1 in list(dict_1):
            if dict_1[k1] > 1:
                del dict_1[k1]

        for k2 in list(dict_2):
            if dict_2[k2] > 1:
                del dict_2[k2]

        count = 0
        for k1,v1 in dict_1.items():
            if k1 in dict_2:
                count+=1
            
        return count