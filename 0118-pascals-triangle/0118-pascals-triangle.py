class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        final_array = []
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1],[1,1]]
        else:
            final_array.append([1])
            final_array.append([1,1])
            for i in range(numRows-2):
                actual_array = []
                last_array = final_array[-1]
                actual_array.append(1)
                for j in range(len(last_array)):
                    
                    if j < len(last_array) - 1:
                        actual_array.append(last_array[j] + last_array[j+1])
                actual_array.append(1)
                final_array.append(actual_array)
        return final_array
