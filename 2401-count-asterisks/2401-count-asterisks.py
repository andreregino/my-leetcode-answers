class Solution:
    def countAsterisks(self, s: str) -> int:
        count_pipes = 0
        final_count = 0
        for letter in s:
            if letter == "|":
                count_pipes += 1
            elif letter == "*" and count_pipes % 2 == 0:
                final_count += 1
        return final_count
