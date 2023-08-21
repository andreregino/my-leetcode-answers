class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict_sum = {}
        for i in nums:
            if i not in dict_sum:
                dict_sum[i] = 1
            else:
                dict_sum[i] = dict_sum[i] + 1

        biggest_count = 0
        biggest_num = 0
        for num, count in dict_sum.items():
            if count > biggest_count:
                biggest_num = num
                biggest_count = count
        return biggest_num