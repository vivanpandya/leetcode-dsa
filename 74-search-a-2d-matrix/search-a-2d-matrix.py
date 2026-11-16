class Solution:
    def searchMatrix(self, matrix, target):
        m = len(matrix)
        n = len(matrix[0])

        left = 0
        right = m * n - 1

        while left <= right:
            mid = (left + right) // 2

            row = mid // n
            col = mid % n

            if matrix[row][col] == target:
                return True

            elif matrix[row][col] < target:
                left = mid + 1

            else:
                right = mid - 1

        return False