class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        final_string = ""
        s = s.split()
        for word in s:
            final_string += word + " "
            k -= 1
            if k == 0:
                break
        return final_string[:-1]
