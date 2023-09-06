class Solution:
    def restoreString(self, word: str, indices: List[int]) -> str:
        final_list = list(word)
        for index, w in enumerate(word):
            final_list[indices[index]] = w
        return "".join(final_list)