class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        if len(d) < 3: return 0
        count = 0
        vals = list(d.keys())
        lenvals = len(vals)
        for i in range(lenvals):
            for j in range(i + 1, lenvals):
                for k in range(j + 1, lenvals):
                    count += (d[vals[i]] * d[vals[j]] * d[vals[k]])
        return count
        