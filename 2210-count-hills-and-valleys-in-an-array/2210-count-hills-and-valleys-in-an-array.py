class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        i = 1
        res = 0
        previous = None
        while i <= len(nums)-1:
            left = i
            right = i
            while left >= 0:
                if nums[left] != nums[i]:
                    break
                left = left - 1
            else:
                i += 1
                continue
            while right < len(nums):
                if nums[right] != nums[i]:
                    break
                right += 1
            else:
                i += 1
                continue
            if nums[left] > nums[i] and nums[right] > nums[i] and previous != 'hill':
                previous = 'hill'
                res += 1
            elif nums[left] < nums[i] and nums[right] < nums[i] and previous != 'valley':
                previous = 'valley'
                res += 1
            i += 1
        return res
            


        