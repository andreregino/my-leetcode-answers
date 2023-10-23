class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sum_n_divisible = 0
        sum_divisible = 0

        for i in range(1, n+1):
            if i % m == 0:
              sum_divisible += i
            else:
              sum_n_divisible += i

        return sum_n_divisible - sum_divisible  
