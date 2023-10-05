class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start_index = 0
        end_index = len(nums) - 1
        while start_index <= end_index:
            middle_index = start_index + ((end_index - start_index) // 2)
            if nums[middle_index] == target:
                return middle_index
            elif target < nums[middle_index]:
                end_index = middle_index - 1
            else:
                start_index = middle_index + 1
            
        return -1