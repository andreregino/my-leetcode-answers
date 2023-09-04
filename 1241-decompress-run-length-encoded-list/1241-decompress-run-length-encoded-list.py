class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        final_array = []
        for index, freq in enumerate(nums):
            
            for k in range(freq):
                if index % 2 == 1:
                    break
                final_array.append(nums[index+1])
        
        return final_array
        