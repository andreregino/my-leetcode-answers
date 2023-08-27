class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        mult = 1
        d = 0
        for digit in digits[::-1]:
            d = d + (digit * mult)
            mult *= 10
        
        d = d + 1
        d = str(d)
        digits = []
        for x in d:
            digits.append(int(x))
        return digits
            