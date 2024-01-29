import sys
class Solution:
    def totalhrs(self,nums, hourly):
        total_hrs = 0
        for i in range(len(nums)):
            total_hrs += ceil(nums[i]/hourly)
        return total_hrs
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        minimum = sys.maxsize
        while (low <= high):
            mid = (low + high) // 2
            temp = self.totalhrs(piles,mid)
            if temp <= h:
                minimum = mid
                high = mid - 1
            else:
                low = mid + 1
        return minimum

        