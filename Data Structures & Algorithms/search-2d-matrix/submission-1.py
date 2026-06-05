class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r, c = len(matrix), len(matrix[0])
        l, r = 0, (r*c) - 1

        while l <= r: 
            midpoint = (l+r) // 2
            row, col = midpoint // c, midpoint % c

            if matrix[row][col] == target:
                return True
            
            if matrix[row][col] > target:
                r = midpoint - 1
            else:
                l = midpoint + 1
        return False
        
        