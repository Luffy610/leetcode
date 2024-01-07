class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i in nums:
            if len(res) == 0:
                res.append([i])
            else:
                for j in res:
                    if i not in j:
                        j.append(i)
                        break
                else:
                    res.append([i])
        return res
        

        