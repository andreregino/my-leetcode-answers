class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        index = 0
        runningSumArray = []
        for num in nums:
            if index != 0:
                runningSumArray.append(runningSumArray[index-1] + num)
            else:
                runningSumArray.append(num)
            index+=1
        return runningSumArray