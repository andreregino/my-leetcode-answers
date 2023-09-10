class Solution:
    def interpret(self, command: str) -> str:
        final_string = ""
        for i, letter in enumerate(command):
            if letter == "G":
                final_string += "G"
            elif letter == "(" and command[i+1] == ")":
                final_string += "o"
            elif letter == "(" and command[i+1] == "a":
                final_string += "al"
        return final_string
        