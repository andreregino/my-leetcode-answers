class Solution:
    def romanToInt(self, s: str) -> int:
        sum_int = 0
        decrease = False
        roman_int_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        for index, roman in enumerate(s):
            if index+1 < len(s) and roman_int_dict[roman] < roman_int_dict[s[index+1]] and decrease == False:
                #print("entrou 1: valor", roman_int_dict[roman], sum_int)
                decrease = True
                continue
            elif decrease == True:
                sum_int += roman_int_dict[roman] - roman_int_dict[s[index-1]]
                #print("entrou 2: valor", roman_int_dict[roman], sum_int)
                decrease = False
            else:
                sum_int += roman_int_dict[roman]
                #print("entrou 3: valor", roman_int_dict[roman], sum_int)
        
        return sum_int