class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1

        while start <= end:
            mid = (start + end) // 2
            if matrix[mid][-1] == target:
                return True
            elif matrix[mid][-1] < target:
                start = mid + 1
            elif matrix[mid][-1] > target:
                end = mid - 1
        
        if start >= len(matrix): 
            return False

        correct_row = matrix[start]
        row_start = 0
        row_end = len(correct_row) - 1

        while row_start <= row_end:
            mid = (row_start + row_end) // 2
            if correct_row[mid] == target:
                return True
            elif correct_row[mid] < target:
                row_start = mid + 1
            elif correct_row[mid] > target:
                row_end = mid - 1
        
        return False

        # Time Complexity: O(log n) + O(log m)
        # Space Complexity: O(1)
