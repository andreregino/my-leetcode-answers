class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        subseq = []
        nums_set = set(nums)
        count = 0
        max_count = 1
        if len(nums) == 0:
            return 0

        for num in nums_set:
            if ((num-1) not in nums_set) and (num+1) in nums_set: #check if is the first of seq
                next_number = num

                while next_number in nums_set: #loop through the sequence
                    count+=1
                    next_number = next_number + 1

                if count > max_count: #updates max count
                    max_count = count
                count = 0
        return max_count