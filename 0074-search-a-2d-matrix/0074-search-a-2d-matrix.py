class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start_index = 0
        end_index = len(matrix) - 1
        while start_index <= end_index:
            middle_index = start_index + ((end_index - start_index) // 2)
            #print("start_index", start_index, end_index, middle_index)
            if matrix[middle_index][0] == target:
                return True
            elif target >= matrix[middle_index][0] and target <= matrix[middle_index][len(matrix[0]) - 1]:
                break
            elif target < matrix[middle_index][0]:
                end_index = middle_index - 1
            else:
                start_index = middle_index + 1
        

        
        
        
        
        start_index_column = 0
        end_index_column = len(matrix[0]) - 1

        while start_index_column <= end_index_column:
            middle_index_column = start_index_column + ((end_index_column - start_index_column) // 2)
            #print("start_index_column", start_index_column, end_index_column, middle_index_column)
            if matrix[middle_index][middle_index_column] == target:
                return True
            elif target < matrix[middle_index][middle_index_column]:
                end_index_column = middle_index_column - 1
            else:
                start_index_column = middle_index_column + 1

        
        return False