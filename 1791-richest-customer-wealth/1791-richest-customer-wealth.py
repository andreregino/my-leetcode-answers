class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        biggest_sum = 0
        height = len(accounts)
        width = len(accounts[0])
        for m in range(height):
            sum = 0
            for n in range(width):
                sum = sum + accounts[m][n]
            if sum > biggest_sum:
                biggest_sum = sum
        return biggest_sum 
