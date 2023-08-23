class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_of_words = {}
        final_list = []
        for word in strs:
            new_word = "".join(sorted(word))
            if new_word not in dict_of_words:
                dict_of_words[new_word] = []
            dict_of_words[new_word].append(word)
        
        for key, value in dict_of_words.items():
            final_list.append(value)

        return final_list
        

