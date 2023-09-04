class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        length = len(mat)
        final_sum = 0
        for i in range(length):
            final_sum += mat[i][i]
            final_sum += mat[i][length-i-1]
        if length % 2 == 1:
            final_sum -= mat[(length // 2)][(length // 2)]
        return final_sum
        