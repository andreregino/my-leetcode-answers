class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        a = s[0:len(s)//2]
        b = s[len(s)//2:]
        dict_vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0, 'A':0, 'E':0, 'I':0, 'O':0, 'U':0, "total": 0}
        
        for letter_a in a:
            if letter_a in dict_vowels:
                dict_vowels["total"] = dict_vowels["total"] + 1
        
        for letter_b in b:
            if letter_b in dict_vowels:
                dict_vowels["total"] = dict_vowels["total"] - 1

        return dict_vowels["total"] == 0
        
        