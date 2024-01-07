class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        ans = []
        while len(grid[0]) > 0:
            del_max = []
            for i in grid:
                temp = max(i)
                i.remove(temp)
                del_max.append(temp)
            ans.append(max(del_max))
        return sum(ans)