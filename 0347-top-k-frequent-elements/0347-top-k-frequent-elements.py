class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dict_nums_freq = {}
        list_high_freq = []

        for num in nums:
            if num not in dict_nums_freq:
                dict_nums_freq[num] = 0
            dict_nums_freq[num] += 1
        
        for i in range(k):
            high_freq_val = 0
            high_freq_index = 0
            for n in list(dict_nums_freq):
                if dict_nums_freq[n] > high_freq_val:
                    high_freq_val = dict_nums_freq[n]
                    high_freq_index = n
            list_high_freq.append(high_freq_index)
            del dict_nums_freq[high_freq_index]

        return list_high_freq
