class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_p = 0
        right_p = len(height) - 1
        max_area = 0
        while left_p < right_p:
            final_height = min(height[left_p], height[right_p])
            final_width = right_p - left_p
            area = final_height * final_width

            if area > max_area:
                max_area = area

            if height[left_p] <= height[right_p]:
                left_p += 1
            else:
                right_p -= 1
        return max_area