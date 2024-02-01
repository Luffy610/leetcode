class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_outer = 0
        right_outer = len(matrix) - 1
        if len(matrix) == 1:
            ans_outer = matrix[0]
        else:
            while(left_outer <= right_outer):
                mid = (left_outer + right_outer) // 2
                if matrix[mid][0] <= target <= matrix[mid][-1]:
                    ans_outer = matrix[mid]
                    break
                elif target < matrix[mid][0]:
                    right_outer = mid - 1
                else:
                    left_outer = mid + 1
            else:
                return False
        left = 0
        right = len(ans_outer) - 1
        while(left <= right):
            mid = (left + right) // 2
            if ans_outer[mid] == target:
                return True
            elif ans_outer[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        else:
            return False

            

        