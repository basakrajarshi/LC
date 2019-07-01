class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        if not matrix:
            return []
        
        rows = len(matrix)
        columns = len(matrix[0])
        matrix_size = rows * columns
        seen = [[False] * columns for _ in matrix]
        result = []
        row = 0
        col = 0
        direction = 0
        dir_row = [0, 1, 0, -1]
        dir_col = [1, 0, -1, 0]
        
        for j in range(matrix_size):
            result.append(matrix[row][col])
            seen[row][col] = True
            next_row = row + dir_row[direction]
            next_col = col + dir_col[direction]
            
            if 0 <= next_row < rows and 0 <= next_col < columns and not seen[next_row][next_col]:
                row = next_row
                col = next_col
            else:
                direction = (direction + 1) % 4
                row = row + dir_row[direction]
                col = col + dir_col[direction]
                
        return result
