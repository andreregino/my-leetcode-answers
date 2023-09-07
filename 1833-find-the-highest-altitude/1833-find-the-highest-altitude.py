class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_alt = 0
        sum_trip = 0
        for g in gain:

            sum_trip += g
            if sum_trip > max_alt:
                max_alt = sum_trip
        
        return max_alt

        