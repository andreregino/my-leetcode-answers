class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        for i, num in enumerate(nums):
            for num_2 in range(i+1, len(nums)):
                if num == nums[num_2]:
                    good_pairs += 1

        return good_pairs