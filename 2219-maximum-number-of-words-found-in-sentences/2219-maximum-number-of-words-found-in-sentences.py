class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_counter = 0
        space_counter = 0
        for sentence in sentences:
            space_counter = sentence.count(" ") + 1
            if space_counter > max_counter:
                max_counter = space_counter

        return max_counter
        