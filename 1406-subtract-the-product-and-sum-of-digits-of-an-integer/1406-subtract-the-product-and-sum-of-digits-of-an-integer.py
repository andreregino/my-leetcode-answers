class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = list(str(n))
        mult = 1
        sum = 0
        for i in n:
            mult *= int(i)
            sum += int(i)
        return mult - sum