# 864
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        cols = len(matrix[0])
        result = [[0] * rows for _ in range(cols)]
        for r in range(rows):
            for c in range(cols):
                result[c][r] = matrix[r][c]
                
        return result

# 566
class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        m = len(mat)
        n = len(mat[0])
        
        # Check if the reshape operation is possible
        if m * n != r * c:
            return mat
            
        # Initialize the new matrix with dimensions r x c
        reshaped = [[0] * c for _ in range(r)]
        
        # Fill the new matrix using flat index mapping
        for i in range(m * n):
            # Extract element from the original matrix
            val = mat[i // n][i % n]
            # Place element into the new matrix
            reshaped[i // c][i % c] = val
            
        return reshaped
