class Solution:
    def sortSentence(self, s: str) -> str:
        
        dict_sentence = {}
        final_sentence = ""
        s = s.split()
        sent_len = len(s)
        for sent in s:
            dict_sentence[int(sent[-1])] = sent[:-1]
        
        for i in range(1, sent_len + 1):
            final_sentence += dict_sentence[i] + " "

        return final_sentence[:-1]