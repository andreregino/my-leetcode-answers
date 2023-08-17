class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_from_list = set(nums)
        if nums == list(set_from_list) or len(nums) == len(list(set_from_list)):
            return False
        return True