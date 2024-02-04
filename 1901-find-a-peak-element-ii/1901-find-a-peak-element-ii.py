class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:

        # initialization useful terms
        M = len(mat)    # rows
        N = len(mat[0]) # columns

        for i in range(M):
            # Binary Search in rows
            low, high = 0, N - 1

            while low < high:
                mid = (low + high) // 2
                if mat[i][mid] > mat[i][mid+1]:
                    high = mid 
                else:
                    low = mid + 1
            
            # element in same column, but in above and below row
            above = mat[i-1][low] if i - 1 >=  0 else -1
            below = mat[i+1][low] if i + 1 < M else -1
            if mat[i][low] > above and mat[i][low] > below:
                return [i,low]
            
        for j in range(N):
            # Binary Search in Columns
            low, high = 0, M - 1

            while low < high:
                mid = ( low + high ) // 2
                if mat[mid][j] > mat[mid+1][j]:
                    high = mid
                else:
                    low = mid + 1
            
            Left = mat[low][j-1] if j-1 >= 0 else -1
            Right = mat[low][j+1] if j+1 < N else -1
            if mat[low][j] > Left and mat[low][j] > Right:
                return [low,j]
        

        return [-1,-1]


        