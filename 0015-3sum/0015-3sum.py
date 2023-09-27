class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        final_list = []
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            left_pointer = i+1
            right_pointer = len(nums) - 1
            while left_pointer < right_pointer:
                if (num + nums[left_pointer] + nums[right_pointer]) == 0:
                    final_list.append([num, nums[left_pointer], nums[right_pointer]])
                    left_pointer += 1
                    while nums[left_pointer] == nums[left_pointer-1] and left_pointer < right_pointer:
                        left_pointer += 1
                elif (num + nums[left_pointer] + nums[right_pointer]) < 0:
                    left_pointer += 1
                else:
                    right_pointer -= 1
        
        return final_list
            


        