class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        if len(g) > 0 and len(s)> 0:
            count = 0
            for i in g:
                for j in s:
                    if j >= i:
                        count = count + 1
                        s.remove(j)
                        break
            return count
        else:
            return 0
        
        