class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        dict_order_heights = {}
        ordered_names = []
        for i, height in enumerate(heights):
            dict_order_heights[height] = i
        
        heights.sort()
        for height in heights[::-1]:
            ordered_names.append(names[dict_order_heights[height]])
        
        return ordered_names

        