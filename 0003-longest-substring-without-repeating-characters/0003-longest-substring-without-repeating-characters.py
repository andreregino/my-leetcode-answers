class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left_pointer = 0
        right_pointer = 1
        max_substr_len = 0 if len(s) == 0 else 1


        while left_pointer != (len(s) - 1) and right_pointer < len(s):
            substr = s[left_pointer:right_pointer+1]
            #print(left_pointer, right_pointer, substr)
            if len(substr) <= max_substr_len: 
                right_pointer += 1
                continue
            if len(set(substr)) == len(substr) and len(substr) > max_substr_len:
                max_substr_len = len(substr)
                right_pointer += 1
            if len(set(substr)) != len(substr) and left_pointer != right_pointer:
                left_pointer += 1
            

        return max_substr_len