class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        decode_dict = {" ": " "}
        final_string = ""
        i = 0
        for k in key:
            if k not in decode_dict:
                decode_dict[k] = alphabet[i]
                i+= 1
        
        for m in message:
            final_string += decode_dict[m]

        return final_string