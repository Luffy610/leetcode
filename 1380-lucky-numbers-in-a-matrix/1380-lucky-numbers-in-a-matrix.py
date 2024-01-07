class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_row = {}
        for i in range(len(matrix)):
            temp = min(matrix[i])
            index = matrix[i].index(temp)
            min_row[temp] = index
        print(min_row)
        for value, column in min_row.items():
            for i in range(len(matrix)):
                if matrix[i][column] > value:
                    break
                else:
                    continue
            else:
                return [value]
                   