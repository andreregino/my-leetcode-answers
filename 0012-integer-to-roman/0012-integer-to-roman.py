class Solution:
    def intToRoman(self, num: int) -> str:
        dict_int_to_roman = {
            1000: "M",
            500: "D",
            100: "C",
            50: "L",
            10: "X",
            5: "V",
            1: "I"
        }

        final_value = ""
        while num != 0:
            for k, v in dict_int_to_roman.items():
                if num >= k:
                    final_value += v
                    num -= k
                    break
        
        final_value = final_value.replace("DCCCC", "CM")
        final_value = final_value.replace("LXXXX", "XC")
        final_value = final_value.replace("VIIII", "IX")
        final_value = final_value.replace("CCCC", "CD")
        final_value = final_value.replace("XXXX", "XL")
        final_value = final_value.replace("IIII", "IV")
        return final_value
