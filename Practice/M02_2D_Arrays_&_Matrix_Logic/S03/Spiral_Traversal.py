# 54
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows,cols=len(matrix),len(matrix[0])
        top,bottom=0,rows-1
        left,right=0,cols-1
        res=[]
        while top<=bottom and left <= right:
            # left->right
            for col in range(left,right+1):
                res.append(matrix[top][col])
            top+=1

            # top->bottom
            for row in range(top,bottom+1):
                res.append(matrix[row][right])
            right-=1

            # right->left
            if top <= bottom:
                for col in range(right,left-1,-1):
                    res.append(matrix[bottom][col])
                bottom -= 1
            # bottom -> top
            if left <= right:
                for row in range(bottom,top-1,-1):
                    res.append(matrix[row][left])
                left+=1
        return res

    
# 59
class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        # Initialize an n x n matrix with zeros
        matrix = [[0] * n for _ in range(n)]
        
        # Define boundaries
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        
        # Start filling from 1 up to n^2
        num = 1
        
        while top <= bottom and left <= right:
            # 1. Traverse from left to right across the top row
            for col in range(left, right + 1):
                matrix[top][col] = num
                num += 1
            top += 1  # Move the top boundary down
            
            # 2. Traverse from top to bottom down the right column
            for row in range(top, bottom + 1):
                matrix[row][right] = num
                num += 1
            right -= 1  # Move the right boundary left
            
            # 3. Traverse from right to left across the bottom row
            for col in range(right, left - 1, -1):
                matrix[bottom][col] = num
                num += 1
            bottom -= 1  # Move the bottom boundary up
            
            # 4. Traverse from bottom to top up the left column
            for row in range(bottom, top - 1, -1):
                matrix[row][left] = num
                num += 1
            left += 1  # Move the left boundary right
            
        return matrix
