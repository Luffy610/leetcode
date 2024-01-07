class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        res = 0
        l  = [[0 for i in range(n)]for i in range(m)]
        for indice in indices:
            row = indice[0]
            col = indice[1]
            for i in range(n):
                l[row][i] += 1
            for j in range(m):
                l[j][col] += 1
        for i in l:
            for j in i:
                if j % 2 == 1:
                    res += 1
        return res
        