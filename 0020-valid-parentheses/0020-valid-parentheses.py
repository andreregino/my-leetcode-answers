class Solution:
    def isValid(self, s: str) -> bool:
        dict_parentheses = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        string_stack = []
        for character in s:
            if character in dict_parentheses:
                if len(string_stack) > 0 and string_stack[-1] == dict_parentheses[character]:
                    string_stack.pop()
                else:
                    return False
            else:
                string_stack.append(character)
        
        if len(string_stack) > 0:
            return False
        return True
        