class Solution:
    def trap(self, height: List[int]) -> int:
        left_p = 0
        right_p = len(height) - 1
        left_max_p = height[left_p]
        right_max_p = height[right_p]
        count_trapping = 0
        while left_p < right_p:
            if left_max_p < right_max_p:
                left_p += 1
                left_max_p = max(left_max_p, height[left_p])
                count_trapping += left_max_p - height[left_p]
            else:
                right_p -= 1
                right_max_p = max(right_max_p, height[right_p])
                count_trapping += right_max_p - height[right_p]

        return count_trapping